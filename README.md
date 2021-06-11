# Dataproc-workflow-template

## Links
https://phoenixnap.com/kb/install-spark-on-ubuntu  
https://sparkbyexamples.com/spark/spark-convert-csv-to-avro-parquet-json/

## spark download:
```bash 
sudo apt install default-jdk scala git -y
wget https://apache.mirror.colo-serv.net/spark/spark-2.4.8/spark-2.4.8-bin-hadoop2.7.tgz
tar xvf spark-*
sudo mv spark-2.4.8-bin-hadoop2.7 /opt/spark
echo "export SPARK_HOME=/opt/spark" >> ~/.profile
echo "export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin" >> ~/.profile
echo "export PYSPARK_PYTHON=/usr/bin/python3" >> ~/.profile
# start master and worker node
/opt/spark/sbin/start-master.sh
# check http://127.0.0.1:8080/
/opt/spark/sbin/start-slave.sh  spark://cs-376442122481-default-default-k4s22:7077
pip3 install pyspark==2.4.8
```

