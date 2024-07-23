import os
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator
from dotenv import load_dotenv
from utils import extract, transform, load

# Set Up Variables
load_dotenv('/opt/airflow/dags/files/.env')
extract_db_config = {
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'host': os.getenv('MYSQL_HOST'),
    'database': os.getenv('MYSQL_DATABASE')
}
load_db_config = {
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'host': os.getenv('MYSQL_HOST'),
    'database': os.getenv('MYSQL_DATABASE')
}
file_path = os.getenv('FILE_PATH')

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2024, 7, 13),
}

dag = DAG(
    dag_id='ETL',
    default_args=default_args,
    description='ETL DAG for processing orders.csv and db data',
    schedule_interval='@daily',  # Or '*/5 * * * *' cron for example
    catchup=False  # Disable catchup to avoid backfilling
)

# Define tasks
extract_data_task = PythonOperator(
    task_id='extract_data_task',
    python_callable=extract.extract_data,
    op_kwargs={'file_path': file_path, 'db_config': extract_db_config},
    dag=dag,
)

transform_data_task = PythonOperator(
    task_id='transform_data_task',
    python_callable=transform.transform_data,
    op_args=[
        extract_data_task.output['orders'],
        extract_data_task.output['categories'],
        extract_data_task.output['sellers'],
        extract_data_task.output['products'],
    ],
    provide_context=True,
    dag=dag,
)

load_data_task = PythonOperator(
    task_id='load_data_task',
    python_callable=load.load_data,
    op_args=[transform_data_task.output, load_db_config],
    provide_context=True,
    dag=dag,
)

send_email_task_failure = EmailOperator(
    task_id='send_email_task_failure',
    to=os.getenv('EMAIL_RECIVER'),
    subject='Airflow Alert: Task Failed',
    html_content='<p>Task {{ task_instance.task_id }} failed in DAG {{ dag.dag_id }} on {{ execution_date }}.</p>',
    trigger_rule='one_failed',
    dag=dag,
)

send_email_task_success = EmailOperator(
    task_id='send_email_task_success',
    to=os.getenv('EMAIL_RECIVER'),
    subject='Airflow Alert: DAG Succeeded',
    html_content='<p>DAG {{ dag.dag_id }} succeeded on {{ execution_date }}.</p>',
    dag=dag,
)

# Define task dependencies
extract_data_task >> transform_data_task >> load_data_task >> send_email_task_failure # If any task fails, send an email
load_data_task >> send_email_task_success # If all tasks are completed, send an email of success
