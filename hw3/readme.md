## map-reduce
dataset: https://www.kaggle.com/datasets/arevel/chess-games (`head -n 1800000`)
мапредьюс: считаем кол-во побед черных в блиц по числам месяца

Запуск локально: `cat <dataset> | python3 <map.py> | sort | python3 <reduce.py>`
Запуск на standalone/кластере:
`hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar -input <dataset> -output output -mapper <map.py> -reducer <reduce.py>`

Local (1 thread): 28sec
Standalone:
Cluster:
