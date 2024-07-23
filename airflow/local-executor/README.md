# Airflow Docker Compose Setup

![Airflow Docker Compose Setup](./image-readme/arch-diag-basic.png)

This setup uses Docker Compose to run Apache Airflow locally. It includes a webserver, scheduler, and PostgreSQL database.

### Setup

1. **Create a `.env` file**

   In the root directory, create a `.env` file with the following environment variables:

   ```dotenv
   POSTGRES_USER=airflow
   POSTGRES_PASSWORD=airflow
   POSTGRES_DB=airflow
   AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:airflow@postgres/airflow
   AIRFLOW__WWW_USER_USERNAME=test
   AIRFLOW__WWW_USER_PASSWORD=test
   AIRFLOW_USER_UID=501
   AIRFLOW_USER_GID=0
   AIRFLOW__SMTP__SMTP_HOST=smtp.gmail.com
   AIRFLOW__SMTP__SMTP_USER=test@gmail.com
   AIRFLOW__SMTP__SMTP_PASSWORD=token test
   AIRFLOW__SMTP__SMTP_MAIL_FROM=test@gmail.com
   AIRFLOW__SMTP__SMTP_PORT=587
   ```

  Modify these variables according to your configuration.

**Start Airflow services**

   Run the following command to start Airflow and related services:

   ```bash
   docker-compose up -d
   ```

   This starts PostgreSQL, Airflow webserver, and scheduler in detached mode.

### Accessing Airflow

- **Airflow Webserver**: [http://localhost:8080](http://localhost:8080)

### Using Airflow API

- **Swagger UI**: [http://localhost:8080/api/v1/ui/#/](http://localhost:8080/api/v1/ui/#/)

- **Endpoints**:
  - **List DAGs**: [http://localhost:8080/api/v1/dags](http://localhost:8080/api/v1/dags)
  - **Trigger DAG**: [POST http://localhost:8080/api/v1/dags/{dag_id}/dagRuns](http://localhost:8080/api/v1/dags/{dag_id}/dagRuns)
  - **List DAG Runs**: [GET http://localhost:8080/api/v1/dags/{dag_id}/dagRuns](http://localhost:8080/api/v1/dags/{dag_id}/dagRuns)
  - **Get DAG Run Details**: [GET http://localhost:8080/api/v1/dags/{dag_id}/dagRuns/{dagrun_id}](http://localhost:8080/api/v1/dags/{dag_id}/dagRuns/{dagrun_id})

### DAG Overview

- **ETL DAG**:
  - **Purpose**: Processes `orders.csv` and data from a MySQL database.
  - **Schedule**: Runs daily (`@daily`). Modify `schedule_interval` in `ETL.py` to change the frequency.
  - **Tasks**:
    - **Extract**: Reads data from a CSV file and a MySQL database.
    - **Transform**: Cleans and merges the data.
    - **Load**: Writes the processed data into a MySQL database.
    - **Email Notifications**: Sends an email on task failure and upon successful completion.

### `.env` for DAGs Folder

In the `dags/files/` folder, create a `.env` file with the following:

```dotenv
FILE_PATH=/opt/airflow/dags/files/orders.csv
EMAIL_RECIVER=test@gmail.com
MYSQL_DATABASE=ecommerce
MYSQL_USER=pass
MYSQL_PASSWORD=pass
MYSQL_HOST=mysql:3306
```
Modify these variables according to your configuration.

### Docker Compose Configuration

- **Networks**: Defined as `bi-project-network`.
- **Services**:
  - **PostgreSQL**: Database service.
  - **Airflow Webserver**: Web interface for Airflow.
  - **Airflow Scheduler**: Handles task scheduling.

### Additional Notes

- **Docker Compose**: Adjust `docker-compose.yml` for scaling or additional services.
- **Security**: For production, secure Airflow with advanced authentication methods.

### Troubleshooting

- Check Airflow logs (`./logs`) and Docker container logs for errors.