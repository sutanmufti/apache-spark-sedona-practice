from pyspark.sql import SparkSession

def main():
    spark = (
    SparkSession.builder
        .appName("Sedona Example")
        .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
        .config("spark.kryo.registrator", "org.apache.sedona.viz.core.Serde.SedonaVizKryoRegistrator")
        .config("spark.sql.extensions", "org.apache.sedona.sql.SedonaSqlExtensions")
        .getOrCreate()
    )

    print("THE SPARK VERSION IS:::", spark.version)
    df = spark.read.parquet('file:///shared/riyadh_places.parquet')
    spark.sql("Select ST_Point(1,1)").show()
    df.createOrReplaceTempView('riyadh')

    spark.sql("Select ST_AsText(ST_GeomFromWKB(geometry)) as riyadh_geometry from riyadh limit 10").show()

    spark.stop()

if __name__=='__main__':
    main()
