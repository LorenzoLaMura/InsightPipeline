# InsightPipeline: ETL Workflow for BI Dashboard 🚀📊

## Overview

Welcome to **InsightPipeline**! This project is all about transforming raw data into actionable insights through a seamless ETL (Extract, Transform, Load) process. By orchestrating data flows with Apache Airflow, analyzing data with Jupyter Notebooks, and visualizing results with Grafana, we bring data to life in a BI (Business Intelligence) dashboard.

![Architecture](./images/BI_Project.jpg)

This project demonstrates a complete data engineering and data analysis workflow using Airflow and Grafana with Docker. It includes the following components:
1. **MySQL** - To store raw and processed data.
2. **Jupyter Notebook** - For initial data analysis and exploratory data analysis (EDA).
3. **Airflow** - To create ETL (Extract, Transform, Load) pipelines.
4. **Grafana** - For visualizing data and creating dashboards.

## Project Structure 📁

The project is divided into four main directories:

- `mysql` 🗄️
- `notebook` 📒
- `airflow` 🌬️
- `grafana` 📊

Each directory contains a `README.md` file with detailed instructions on how to run the respective component.

## Workflow 🔄

### 1. Data Sources 📂

The project uses two data sources:
- A MySQL database 🗃️
- A CSV file 📑

### 2. Data Analysis 🔍

Data is first analyzed using Jupyter Notebooks. This step includes:
- Exploring the raw data 🧐
- Cleaning and preprocessing the data 🧹
- Performing initial transformations and analysis 🔬

### 3. ETL Pipeline 🚚

Apache Airflow is used to automate the ETL process. The ETL pipeline includes:
- **Extract**: Reading data from the MySQL database and CSV file. 📤
- **Transform**: Cleaning, merging, and transforming the data. 🛠️
- **Load**: Loading the processed data back into the MySQL database. 📥

### 4. Data Visualization 📈

Grafana is used to visualize the processed data. Dashboards are created to provide insights and track key metrics. 📊

## Running the Project 🏃‍♂️

The entire project can be run using Docker and Docker Compose. This ensures a consistent and reproducible environment.

### Setup ⚙️

1. **Clone the repository:**
    ```bash
    git clone https://github.com/LorenzoLaMura/InsightPipeline
    cd InsightPipeline
    ```

2. **Navigate to each component's directory and follow the instructions in its `README.md` file** to set up and run the individual services:

   - **MySQL**: Set up and run the MySQL database. 🗄️
   - **Airflow**: Set up and run the Airflow service. 🌬️
   - **Grafana**: Set up and run the Grafana service. 📊

## Aim 🎯

The aim of this project is to test and demonstrate a complete data engineering and data analysis architecture using Airflow and Grafana with Docker. This allows me to enhance my skills in Docker, Airflow (using Python), Grafana, and data analysis in general.

## Evolution Plan 🛤️

1. **Apache Spark & PySpark** 🚀

    *Idea*: Incorporate Spark for handling large-scale data transformations.
    
    *Reason*: To leverage distributed computing for improved performance.
    
    *Implementation*: Use PySpark to transform data before loading into the target database.

2. **Kafka and CDC (Change Data Capture)** 📡

    *Idea*: Integrate Kafka for real-time data streaming and CDC for tracking changes in MySQL.
    
    *Reason*: To handle real-time data updates and ensure the dashboard reflects the latest information.
    
    *Implementation*: Use Kafka with tools like Debezium or Maxwell's Daemon for CDC.

3. **Monitoring Tools** 🔍

    *Idea*: Implement monitoring tools to track the performance and health of the ETL pipeline.

    *Reason*: To ensure reliability and quickly address any issues.
       
    *Implementation*: Use tools like Prometheus and Grafana for monitoring.

## License 📝

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Acknowledgements 🙏

- [Apache Airflow](https://airflow.apache.org/) 🌬️
- [Docker](https://www.docker.com/) 🐳
- [Grafana](https://grafana.com/) 📊
- [Jupyter](https://jupyter.org/) 📒