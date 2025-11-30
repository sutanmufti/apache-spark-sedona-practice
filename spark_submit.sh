#!/bin/bash

docker exec -it \
  sedona-master \
  /opt/spark/bin/spark-submit \
    --master spark://sedona-master:7077 \
    /jobs/job.py
