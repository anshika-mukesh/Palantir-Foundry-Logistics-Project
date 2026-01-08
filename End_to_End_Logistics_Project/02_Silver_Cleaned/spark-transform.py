from transforms.api import transform, Input, Output
from pyspark.sql import functions as F


@transform(
    raw_sales=Input("/CADEdge-6268f1/End_to_End_Logistics_Project/01_Bronze_Raw/SuperMarket Analysis"),
    cleaned_sales=Output("/CADEdge-6268f1/End_to_End_Logistics_Project/02_Silver_Cleaned/cleaned_inventory")
)
# data files
def my_pipeline(raw_sales, cleaned_sales):
    df = raw_sales.dataframe()
    cleaned_df = df.withColumnRenamed("Invoice ID", "invoice_id") \
        .withColumnRenamed("Product line", "category") \
        .withColumn("stock_level", 100 - F.col("Quantity"))
    cleaned_sales.write_dataframe(cleaned_df)

