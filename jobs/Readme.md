# Shared

`sedona-master` must be able to read job.py using the container's `spark-submit`.


```bash
docker exec -it \
  sedona-master \
  /opt/spark/bin/spark-submit \
    --master spark://sedona-master:7077 \
    /jobs/job.py
```