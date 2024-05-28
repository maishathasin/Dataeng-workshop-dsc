


from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, col


def main():
    spark = SparkSession.builder.appName("WeatherDataProcessing").getOrCreate()

    # Read the JSON data
    df = spark.read.json("./weather_data.json")

    # Flatten the outer `hourly` array
    df_outer = df.select(
        col("latitude"),
        col("longitude"),
        col("generationtime_ms"),
        col("utc_offset_seconds"),
        col("timezone"),
        col("timezone_abbreviation"),
        col("elevation"),
        explode("hourly.temperature_2m").alias("temperature_2m"),
        col("hourly.time").alias("hourly_time")
    )

    # Flatten the nested `time` array
    df_flattened = df_outer.select(
        col("latitude"),
        col("longitude"),
        col("generationtime_ms"),
        col("utc_offset_seconds"),
        col("timezone"),
        col("timezone_abbreviation"),
        col("elevation"),
        col("temperature_2m"),
        explode("hourly_time").alias("time")
    )

    # Write the processed data to a CSV file
    df_flattened.write.csv("processed_weather_data.csv", header=True)

if __name__ == "__main__":
    main()

