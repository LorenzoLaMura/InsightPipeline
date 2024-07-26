import os
import json
from kafka import KafkaConsumer
from airflow_client.client import ApiClient
from dotenv import load_dotenv

# Set Up Variables
load_dotenv('/app/.env')
KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS')
AIRFLOW_API_URL = os.getenv('AIRFLOW_API_URL')
DAG_ID = os.getenv('DAG_ID')
MYSQL_TABLES = os.getenv('MYSQL_TABLES').split(',')


def trigger_dag(dag_id):
    configuration = ApiClient.get_default_configuration()
    configuration.host = AIRFLOW_API_URL
    client = ApiClient(configuration)
    client.post_dag_run(dag_id=dag_id, dag_run={})
    print(f'Triggered DAG: {dag_id}')


def main():
    consumer = KafkaConsumer(
        bootstrap_servers=[KAFKA_BOOTSTRAP_SERVERS],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='airflow-trigger',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    # Subscribe to topics for specified tables
    topics = [f'mysqlserver1.{table}' for table in MYSQL_TABLES]
    consumer.subscribe(topics)
    print(f'Listening for changes on topics: {topics}')

    for message in consumer:
        topic = message.topic
        table_name = topic.split('.')[-1]
        print(f'Received change event for table {table_name}: {message.value}')
        trigger_dag(DAG_ID)


if __name__ == "__main__":
    main()
