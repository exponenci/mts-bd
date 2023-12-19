from datetime import timedelta, datetime
import airflow
from airflow import DAG
from airflow.contrib.operators.ssh_operator import SSHOperator

default_args = {
            'owner': 'airflow',
            'depends_on_past': False,
            'email': ['airflow@example.com'],
            'email_on_failure': False,
            'email_on_retry': False,
            'start_date': '2023-12-05',
            'retries': 1,
            'retry_delay': timedelta(minutes=6000),
            'catchup': False
}

dag = DAG(dag_id='testing_stuff',
          default_args=default_args,
          schedule_interval='50 * * * *',
          dagrun_timeout=timedelta(seconds=1200)) # increase timeout

# TODO download file properly
dataset_url = "https://drive.google.com/uc?export=download&id=1YxOAHarAWmEpYMN08L9I_UiXaYM6SbCt" # set data url
file_name = "beers.csv" # TODO Change filename

# change curl to wget
t1_bash = f"""
wget -O out_file.zip '{dataset_url}'
"""
t2_bash = "unzip -o out_file.zip"

# set PATH and make hadoop directory 
t3_bash = f"""export PATH="$PATH:/usr/local/hadoop/bin" &&
    hdfs dfs -mkdir -p /user/hadoop/from_airflow
    hdfs dfs -put -f {file_name} /user/hadoop/from_airflow"""

t4_bash = "echo 'Hello world!'" # TODO Launch map-reduce properly

t5_bash = "rm out_file.zip"
t6_bash = "rm *.csv"

t1 = SSHOperator(ssh_conn_id='ssh_default',
                 task_id='get_dataset_from_web',
                 command=t1_bash,
                 dag=dag)

t2 = SSHOperator(ssh_conn_id='ssh_default',
                 task_id='unpack_archive',
                 command=t2_bash,
                 cmd_timeout=300,
                 dag=dag)

t3 = SSHOperator(ssh_conn_id='ssh_default',
                 task_id='load_to_hdfs',
                 command=t3_bash,
                 cmd_timeout=300,
                 dag=dag)

t4 = SSHOperator(ssh_conn_id='ssh_default',
                 task_id='run_MR_job',
                 command=t4_bash,
                 dag=dag)

t5 = SSHOperator(ssh_conn_id='ssh_default',
                 task_id='delete_archive',
                 command=t5_bash,
                 dag=dag)


t6 = SSHOperator(ssh_conn_id='ssh_default',
                 task_id='delete_csv',
                 command=t6_bash,
                 dag=dag)

t1 >> t2 >> t3 >> t4 >> t5 >> t6