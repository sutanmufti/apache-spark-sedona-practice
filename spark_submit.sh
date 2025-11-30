#!/bin/bash

# simple job
docker exec -it \
  sedona-master \
  /opt/spark/bin/spark-submit \
    --master spark://sedona-master:7077 \
    --jars /shared/jar/gcs-connector-hadoop3-2.2.25-shaded.jar \
    --conf spark.hadoop.fs.gs.impl=com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem \
    --conf spark.hadoop.fs.AbstractFileSystem.gs.impl=com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS \
    /jobs/job.py



# Read and write to gcs
# read about the connector https://github.com/GoogleCloudDataproc/hadoop-connectors/blob/master/gcs/INSTALL.md
# https://docs.cloud.google.com/dataproc/docs/concepts/connectors/cloud-storage
# set environment GCS_BUCKET_NAME to set the gcs bucket name
docker exec -it \
  sedona-master \
  /opt/spark/bin/spark-submit \
    --master spark://sedona-master:7077 \
    --jars /shared/jar/gcs-connector-hadoop3-2.2.25-shaded.jar \
    --conf spark.app.gcsBucket=$GCS_BUCKET_NAME \
    --conf spark.hadoop.fs.gs.impl=com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem \
    --conf spark.hadoop.fs.AbstractFileSystem.gs.impl=com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS \
    --conf spark.hadoop.google.cloud.auth.service.account.enable=true \
    --conf spark.hadoop.google.cloud.auth.service.account.json.keyfile=/shared/keys/key.json \
    /jobs/write_to_gcs.py
