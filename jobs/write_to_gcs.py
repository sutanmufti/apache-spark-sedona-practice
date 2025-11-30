# MIT License
# Copyright (c) 2025 Sutan Mufti
#
# See the LICENSE file in the project root for full license information.
'''
Author: Sutan Mufti
Date Created: 2025-11-30

Executes the primary Spark job for reading, processing, and sampling
geospatial data stored in Google Cloud Storage (GCS).

This function initialises a Spark session configured with Apache Sedona
extensions, retrieves the target GCS bucket from Spark configuration, and
validates that it has been provided. If no bucket is specified, the job
terminates early.

When a valid bucket is available, the function reads a Parquet dataset
containing Riyadh geospatial records, registers it as a temporary SQL view,
and runs a sample Sedona SQL query to display a subset of geometries in
Well-Known Text (WKT) format.

It then writes a sample of ten records back to a designated output
directory within the same GCS bucket.

Returns:
    int: 0 on successful completion, or 1 if the required configuration
    is missing.

'''

from pyspark.sql import SparkSession

def main():
    '''
    Main function. Runs the job.
    '''

    print("starting job")
    spark = (
    SparkSession.builder
        .appName("Sedona Example")
        .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
        .config("spark.kryo.registrator",
            "org.apache.sedona.viz.core.Serde.SedonaVizKryoRegistrator")
        .config("spark.sql.extensions", "org.apache.sedona.sql.SedonaSqlExtensions")
        .getOrCreate()
    )

    gcs_bucket = spark.conf.get("spark.app.gcsBucket", None)

    if gcs_bucket is None:
        print(r"spark.app.gcsBucket is None. There is no bucket")
        spark.stop()
        return 1
    else:
        print("USING GCS", gcs_bucket)

    df = spark.read.parquet(f"gs://{gcs_bucket}/riyadh_places.parquet")
    df.createOrReplaceTempView('riyadh')
    spark.sql("""
        Select ST_AsText(ST_GeomFromWKB(geometry)) as riyadh_geometry 
        from riyadh limit 10
    """).show()

    output_path = f"gs://{gcs_bucket}/output/riyadh_sample2"

    print("write to gcs")
    sample_df = df.limit(10)
    sample_df.write.mode("overwrite").parquet(output_path)
    print("write done")

    spark.stop()
    return 0

if __name__=='__main__':
    main()
