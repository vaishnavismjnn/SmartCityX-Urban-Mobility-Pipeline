from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "vaishnavi",
    "start_date": datetime(2026, 7, 14),
    "retries": 1
}

with DAG(
    dag_id="smartcity_pipeline",
    default_args=default_args,
    schedule="@daily",
    catchup=False,
    tags=["SmartCityX", "Kafka"],
) as dag:

    run_kafka_producer = BashOperator(
        task_id="run_kafka_producer",
        bash_command='python /opt/airflow/kafka/airflow_producer.py'
    )

    run_kafka_producer