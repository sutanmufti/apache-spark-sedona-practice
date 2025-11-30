# MIT License
# Copyright (c) 2025 Sutan Mufti
#
# See the LICENSE file in the project root for full license information.
"""
This script demonstrates a simple Apache Spark job using Apache Sedona to
process geospatial data stored in Parquet format.

The job initialises a Spark session configured with Sedona's SQL extension
and Kryo serialisation, reads a local Parquet file containing geospatial
records for the Riyadh region, and registers the data as a temporary SQL
view. It then executes a small selection of Sedona SQL functions, including
creating a sample geometry and converting Well-Known Binary (WKB) geometry
fields to Well-Known Text (WKT) for inspection.

The script concludes by printing the Spark version and displaying a short
sample of processed geometries before shutting down the Spark session.

This example is intended for demonstration and portfolio purposes, showing
basic Sedona integration and geospatial querying within a Spark environment.
"""

from pyspark.sql import SparkSession

def main():
    """
    main function
    """
    spark = (
    SparkSession.builder
        .appName("Sedona Example")
        .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
        .config("spark.kryo.registrator",
        "org.apache.sedona.viz.core.Serde.SedonaVizKryoRegistrator")
        .config("spark.sql.extensions", "org.apache.sedona.sql.SedonaSqlExtensions")
        .getOrCreate()
    )

    print("THE SPARK VERSION IS:::", spark.version)
    df = spark.read.parquet('file:///shared/riyadh_places.parquet')
    spark.sql("Select ST_Point(1,1)").show()
    df.createOrReplaceTempView('riyadh')

    spark.sql("""
        Select ST_AsText(ST_GeomFromWKB(geometry)) as riyadh_geometry 
        from riyadh limit 10
    """).show()

    spark.stop()

if __name__=='__main__':
    main()
