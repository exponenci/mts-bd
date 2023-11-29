1. Установка. На каждой машине:
    1. в `install.sh` выставить адреса хостов
    2. запустить скрипт
2. Настройка ssh (внутренние обращения в хадупе через ssh). На мастере из пользователя `hadoop`:
    1. генерируем ключи: `ssh-keygen`.
    2. Копируем публичный ключ на локальный компьютер: `ssh-copy-id localhost`
    3. копируем ключи на слейв-ноды: `scp -r .ssh hadoop@haddop2:~ & scp -r .ssh hadoop@haddop3:~`
3. Заполняем конфиги хадупа:
    1. `/usr/local/hadoop/etc/hadoop/core-site.xml` (урл для NN)
        ```
        <!-- Put site-specific property overrides in this file. -->

        <configuration>
        <property>
            <name>fs.default.name</name>
            <value>hdfs://haddop1:9000</value>
        </property>
        </configuration>
        ```
    2. `/usr/local/hadoop/etc/hadoop/hdfs-site.xml` (директории для NN и DN)
        ```
        <!-- Put site-specific property overrides in this file. -->

        <configuration>
        <property>
            <name>dfs.replication</name>
            <value>3</value>
        </property>
        <property>
            <name>dfs.name.dir</name>
            <value>file:///hadoop/hdfs/namenode</value>
        </property>
        <property>
            <name>dfs.data.dir</name>
            <value>file:///hadoop/hdfs/datanode</value>
        </property>
        </configuration>
        ```
    3. `/usr/local/hadoop/etc/hadoop/mapred-site.xml`
        ```
        <!-- Put site-specific property overrides in this file. -->

        <configuration>
        <property>
            <name>mapreduce.framework.name</name>
            <value>yarn</value>
        </property>
        </configuration>
        ```
    4. `/usr/local/hadoop/etc/hadoop/yarn-site.xml`
        ```
        <configuration>

        <!-- Site specific YARN configuration properties -->
        <property>
            <name>yarn.nodemanager.aux-services</name>
            <value>mapreduce_shuffle</value>
        </property>
        </configuration>
        ```
4. Создаем ФС. На мастере из пользователя `hadoop`:
    1. создаем ФС: `/usr/local/hadoop/bin/hdfs namenode -format`
    2. запускаем кластер:
        ```
        /usr/local/hadoop/sbin/start-dfs.sh
        /usr/local/hadoop/sbin/start-yarn.sh
        ```
5. Автозапуск сервиса (по systemctl). На мастере:
    1. `/etc/systemd/system/hadoop.service`:
        ```
        [Unit]
        Description=Hdfs service
        After=network.target

        [Service]
        Type=forking
        User=hadoop
        Group=hadoop
        ExecStart=/usr/local/hadoop/sbin/start-all.sh
        ExecStop=/usr/local/hadoop/sbin/stop-all.sh
        ExecReload=/bin/kill -HUP $MAINPID
        Restart=on-failure

        [Install]
        WantedBy=multi-user.target
        ```
    2. `systemctl daemon-reload & systemctl enable hadoop`

PS:
1. можно после запуска потыкать по:
    - http://{master-addr}:8088/cluster/nodes
    - http://{master-addr}:9870/dfshealth.html#tab-overview
2. посмотреть на ФС:
    - `hdfs dfs -ls -R /`
3. положить файл в ФС:
    - `hdfs dfs -put /source/path/file /destination/path/file`
