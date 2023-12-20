Меняем некоторые конфиги:

- в `/usr/local/hadoop/etc/hadoop/mapred-site.xml` добавить:
```
<property>
    <name>mapreduce.map.env</name>
    <value>HADOOP_MAPRED_HOME=${HADOOP_HOME}</value>
</property>
<property>
    <name>mapreduce.reduce.env</name>
    <value>HADOOP_MAPRED_HOME=${HADOOP_HOME}</value>
</property>
<property>
    <name>yarn.app.mapreduce.am.resource.mb</name>
    <value>4096</value>
</property>
<property>
    <name>yarn.app.mapreduce.am.command-opts</name>
    <value>-Xmx3768m</value>
</property>
<property>
    <name>mapreduce.map.cpu.vcores</name>
    <value>2</value>
</property>
<property>
    <name>mapreduce.reduce.cpu.vcores</name>
    <value>2</value>
</property>
```
- в `/usr/local/hadoop/etc/hadoop/yarn-site.xml` добавить:
```
<property>
    <name>yarn.resourcemanager.hostname</name>
    <value>haddop1</value>
</property>
<property>
    <name>yarn.acl.enable</name>
    <value>0</value>
</property>
<property>
    <name>yarn.nodemanager.resource.memory-mb</name>
    <value>4096</value>
</property>
<property>
    <name>yarn.nodemanager.resource.cpu-vcores</name>
    <value>2</value>
</property>
<property>
    <name>yarn.scheduler.minimum-allocation-mb</name>
    <value>4096</value>
</property>
```
- копируем эти файлы в другие ноды с помощью scp:
```
> scp /usr/local/hadoop/etc/hadoop/mapred-site.xml haddop2:/usr/local/hadoop/etc/hadoop/mapred-site.xml
> scp /usr/local/hadoop/etc/hadoop/mapred-site.xml haddop3:/usr/local/hadoop/etc/hadoop/mapred-site.xml
> scp /usr/local/hadoop/etc/hadoop/yarn-site.xml haddop2:/usr/local/hadoop/etc/hadoop/yarn-site.xml
> scp /usr/local/hadoop/etc/hadoop/yarn-site.xml haddop3:/usr/local/hadoop/etc/hadoop/yarn-site.xml
```
- перезапускаем yarn:
```
> /usr/local/hadoop/sbin/stop-yarn.sh
> /usr/local/hadoop/sbin/start-yarn.sh
```
