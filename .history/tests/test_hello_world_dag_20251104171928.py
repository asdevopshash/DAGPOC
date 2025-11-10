# Filename: test_hello_dag.py

import pytest
from airflow.models.dag import DAG
from airflow.utils.dag_cycle_tester import check_cycle
from datetime import timedelta

# Import the DAG object from your definition file
from dags.etl.helloworld_dag import dag as hello_world_dag

def test_dag_integrity():
    """Test that the DAG loads without cycles and has the correct metadata."""
    
    # 1. Check for cycles (Airflow utility function)
    # A DAG must not have cycles to be valid.
    check_cycle(hello_world_dag)
    
    # 2. Verify basic DAG properties
    assert hello_world_dag.dag_id == "hello_world_dag"
    assert hello_world_dag.schedule == timedelta(days=1)
    assert hello_world_dag.catchup is False
    assert "hello world" in hello_world_dag.tags
    
    # 3. Verify the number of tasks
    tasks = hello_world_dag.tasks
    assert len(tasks) == 3
    task_ids = [t.task_id for t in tasks]
    assert sorted(task_ids) == sorted(['start_greeting', 'say_hello', 'end_greeting'])

# Filename: test_hello_dag.py (append to the previous file)

def test_task_dependencies():
    """Test that tasks are connected in the correct order."""
    
    dag = hello_world_dag
    
    start_task = dag.get_task("start_greeting")
    hello_task = dag.get_task("say_hello")
    end_task = dag.get_task("end_greeting")

    # Check upstream dependencies
    # hello_task should have start_task as an upstream dependency
    assert start_task.task_id in hello_task.upstream_task_ids
    
    # end_task should have hello_task as an upstream dependency
    assert hello_task.task_id in end_task.upstream_task_ids

    # Check downstream dependencies
    # start_task should have hello_task as a downstream dependency
    assert hello_task.task_id in start_task.downstream_task_ids
