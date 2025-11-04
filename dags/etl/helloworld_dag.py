from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def print_hello():
    """A simple Python function to print 'Hello, World!'."""
    print("Hello, World!")

with DAG(
    dag_id='hello_world_dag',
    start_date=datetime(2023, 1, 1),
    schedule=timedelta(days=1),
    catchup=False,
    tags=['hello world'],
) as dag:
    # A BashOperator to execute a simple bash command
    start_task = BashOperator(
        task_id='start_greeting',
        bash_command='echo "Starting the DAG..."',
    )

    # A PythonOperator to call the print_hello function
    hello_task = PythonOperator(
        task_id='say_hello',
        python_callable=print_hello,
    )

    # Another BashOperator for a concluding message
    end_task = BashOperator(
        task_id='end_greeting',
        bash_command='echo "DAG finished!"',
    )

    # Define task dependencies
    start_task >> hello_task >> end_task