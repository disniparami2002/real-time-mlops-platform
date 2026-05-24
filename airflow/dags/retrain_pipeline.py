from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'disni',
    'start_date': datetime(2026, 5, 23)
}

dag = DAG(
    'customer_churn_retraining_pipeline',
    default_args=default_args,
    schedule='@daily',
    catchup=False
)

train_model = BashOperator(
    task_id='train_model',
    bash_command='python src/train.py',
    dag=dag
)