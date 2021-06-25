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

python3 main.py

create dataproc autoscaling policy and use gcloud to fetch policy uri
gcloud beta dataproc autoscaling-policies list --region northamerica-northeast1
gcloud beta dataproc autoscaling-policies describe policy-0625 --region northamerica-northeast1
projects/sps-sb/regions/us-central1/autoscalingPolicies/policy-0625

create bucket called dataproc-workflow-template-test
gsutil -m cp -r ./pyspark_job/ gs://dataproc-workflow-template-test/

test managed dataproc cluster
gcloud dataproc workflow-templates instantiate-from-file \
    --file=dataproc_workflow_template.yml \
    --region=northamerica-northeast1
```

