from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os
import logging
import requests
import json

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 5, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'data_ingestion_dag',
    default_args=default_args,
    description='A simple data ingestion DAG',
    schedule_interval=None,  # Change this if you want to do batch ingestion, Right Now its at None so you would have to trigger the DAG manually 
    catchup=False,  # No backfill
)

def ingest_data(**kwargs):
    logging.info("Starting data ingestion task")
    url = 'https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&hourly=temperature_2m'
    try:
        response = requests.get(url)
        logging.info(f"Received response with status code: {response.status_code}")
        data = response.json()
        logging.info(data)
        os.makedirs('/data', exist_ok=True)
        with open('/data/weather_data.json', 'w') as f:
            json.dump(data, f)
        logging.info("Data successfully written to file")
    except Exception as e:
        logging.error(f"Error during data ingestion: {e}")

start = EmptyOperator(task_id='start', dag=dag)

ingest_task = PythonOperator(
    task_id='ingest_data',
    python_callable=ingest_data,
    dag=dag,
    execution_timeout=timedelta(minutes=10),  
    provide_context=True, 
)

start >> ingest_task
    