from __future__ import annotations
from datetime import datetime

import pendulum

from airflow.models.dag import DAG
from airflow.providers.ssh.operators.ssh import SSHOperator

with DAG(
    dag_id="ssh_task",
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    schedule=None,
    catchup=False,
    tags=["ssh", "example"],
) as dag:
    
    ssh_task = SSHOperator(
        task_id="ssh_to_server_and_run_commands",
        ssh_conn_id="172.16.5.12",
        command="ls -l && pwd",
        do_xcom_push=True,
    )