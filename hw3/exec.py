import time
import subprocess


dataset_path_local = '/home/hadoop/hw3dataset/chess_dataset.csv'
dataset_path_hdfs = '/input.csv'
map_path = '/home/hadoop/hw3dataset/map.py'
reduce_path = '/home/hadoop/hw3dataset/reduce.py'


def timer(func):
    start = time.time()
    output = func()
    consumed_time = time.time() - start
    return output, consumed_time


def exec_no_hadoop():
    proc = subprocess.Popen('cat {} | python3 {} | sort | python3 {}'.format(dataset_path_local, map_path, reduce_path),
                            stdout=subprocess.PIPE,
                            shell=True)
    return proc.communicate()[0].decode()


def exec_hadoop():
    cmd = 'hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
        -input {} -output output -mapper {} -reducer {}'.format(dataset_path_hdfs, map_path, reduce_path)
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    return proc.communicate()[0].decode()


if __name__ == '__main__':
    output, timing = timer(exec_no_hadoop)
    print(output)
    print()
    print('time consumed (via python lib): ', timing)
