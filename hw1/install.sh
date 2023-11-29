sudo apt update
sudo apt -y upgrade

# setting up ports
sudo iptables -I INPUT -p tcp --dport 9870 -j ACCEPT
sudo iptables -I INPUT -p tcp --dport 8020 -j ACCEPT
sudo iptables -I INPUT -p tcp --match multiport --dports 9866,9864,9867 -j ACCEPT
sudo apt -y install iptables-persistent
sudo netfilter-persistent save

# installing java & hadoop; setting up hadoop
sudo apt -y install default-jdk

cd ~/ && wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz
sudo mkdir /usr/local/hadoop
sudo tar -zxf hadoop-*.tar.gz -C /usr/local/hadoop --strip-components 1
echo "creating hadoop user"
sudo useradd hadoop -m
echo "set hadoop password"
sudo passwd hadoop
chown -R hadoop:hadoop /usr/local/hadoop

echo "\
export HADOOP_HOME=/usr/local/hadoop
export HADOOP_HDFS_HOME=\$HADOOP_HOME
export HADOOP_MAPRED_HOME=\$HADOOP_HOME
export HADOOP_COMMON_HOME=\$HADOOP_HOME
export HADOOP_COMMON_LIB_NATIVE_DIR=\$HADOOP_HOME/lib/native
export HADOOP_OPTS=\"\$HADOOP_OPTS -Djava.library.path=\$HADOOP_HOME/lib/native\"
export YARN_HOME=\$HADOOP_HOME
export PATH=\"\$PATH:\${HADOOP_HOME}/bin:\${HADOOP_HOME}/sbin\"\
" > /etc/profile.d/hadoop.sh

echo "\nexport JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64" >> /usr/local/hadoop/etc/hadoop/hadoop-env.sh

# setting up hosts
echo "\
# 127.0.1.1 hadoop1

<addr1> haddop1
<addr2> haddop2
<addr3> haddop3
" > /etc/hosts


# creating dirs for hdfs
mkdir -p /hadoop/hdfs/{namenode,datanode}
chown -R hadoop:hadoop /hadoop

# enum worker-nodes
echo "\
haddop1
haddop2
haddop3
" > /usr/local/hadoop/etc/hadoop/workers

