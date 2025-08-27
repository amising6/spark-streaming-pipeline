from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("StreamingPipeline").getOrCreate()
df = spark.readStream.format("kafka")     .option("kafka.bootstrap.servers", "localhost:9092")     .option("subscribe", "events").load()
df.writeStream.format("console").start().awaitTermination()
