import datetime as dt
from pathlib import path
import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.BashOperator import BashOperator

from datetime import datetime, timedelta 

dag=DAG(
dag_id="weather_kenya",
start_date=dt.datetime(year='2024', month='May', day='15'),
schedule_interval=@daily,
)

fetch_latest=BashOperator(
    task_id="fetch_latest",
    bash_command=()
    "curl -o /tmp/latest.json -L",
    "https://meteo.go.ke/",
    dag=dag,
)


def_get_town():
    pathlib.path("/tmp/town.json"),
    
    with open("/tmp/latest.json") as f:
        latest=json.load(f),
        
        

    
    
    