from pyspark.sql import SparkSession
import os

def main():
    print("starting job")
    spark = (
    SparkSession.builder
        .appName("Sedona Example")
        .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
        .config("spark.kryo.registrator", "org.apache.sedona.viz.core.Serde.SedonaVizKryoRegistrator")
        .config("spark.sql.extensions", "org.apache.sedona.sql.SedonaSqlExtensions")
        .getOrCreate()
    )

    gcs_bucket = spark.conf.get("spark.app.gcsBucket", None)

    if gcs_bucket == None:
        print(r"os.getenv('GCS_BUCKET') is None. There is no bucket")
        spark.stop()
        return 1
    else:
        print("USING GCS", gcs_bucket)

    df = spark.read.parquet(f"gs://{gcs_bucket}/riyadh_places.parquet")
    df.createOrReplaceTempView('riyadh')
    spark.sql("Select ST_AsText(ST_GeomFromWKB(geometry)) as riyadh_geometry from riyadh limit 10").show()

    output_path = f"gs://{gcs_bucket}/output/riyadh_sample2"

    print("write to gcs")
    sample_df = df.limit(10)
    sample_df.write.mode("overwrite").parquet(output_path)
    print("write done")

    spark.stop()

if __name__=='__main__':
    main()
