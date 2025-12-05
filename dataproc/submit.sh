

gcloud storage cp ./jobs.py gs://$BUCKET/jobs/jobs.py


gcloud dataproc jobs submit pyspark \
    gs://$BUCKET/jobs/jobs.py \
    --cluster=$CLUSTERNAME  \
    --region=$CLUSTERREGION \
    --properties=^£^spark.jars.packages='org.apache.sedona:sedona-spark-shaded-3.5_2.12:1.8.0,org.datasyslab:geotools-wrapper:1.8.0-33.1'
    # ^£^ tells gcloud that the delimiter of the value is £ which is an arbitrary symbol. The problem is that gcloud parses , as a delimiter by default. So we need to tell gcloud that the delimiter to the dict is not , but £.