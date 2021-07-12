from datetime import datetime,timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'zheng',
    'depends_on_past': False,
    'email': ['zheng@drvnintelligence.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date':datetime(2021,7,1)
}

with DAG(
    'dataproc-workflow-demo',
    default_args=default_args,
    schedule_interval=None,
) as dag:
    t1 = BashOperator(
    task_id = 'trigger-dataproc',
    bash_command = 'gcloud dataproc workflow-templates instantiate-from file --file=/home/airfow/gcs/dataproc-workflow-template-test/dataproc_workflow_template/dataproc_workflow_template.yml',
    dag=dag
    )
    