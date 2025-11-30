from pyspark.sql import SparkSession
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/shared/keys/key.json'

def main():
    spark = (
    SparkSession.builder
        .appName("Sedona Example")
        .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
        .config("spark.kryo.registrator", "org.apache.sedona.viz.core.Serde.SedonaVizKryoRegistrator")
        .config("spark.sql.extensions", "org.apache.sedona.sql.SedonaSqlExtensions")
        .getOrCreate()
    )

    df = spark.read.parquet('file:///shared/riyadh_places.parquet')
    df.createOrReplaceTempView('riyadh')
    spark.sql("Select ST_AsText(ST_GeomFromWKB(geometry)) as riyadh_geometry from riyadh limit 10").show()

    output_path = "gs://sample-apache-sedona-bucket-x992jnsd/output/riyadh_sample"

    print("write to gcs")
    sample_df = df.limit(10)
    sample_df.write.mode("overwrite").parquet(output_path)
    print("write done")

    spark.stop()

if __name__=='__main__':
    main()
