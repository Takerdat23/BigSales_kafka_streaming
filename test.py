import time
import json
import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
from kafka import KafkaConsumer
from kafka import KafkaProducer, KafkaConsumer
from pyspark.sql import SparkSession
import joblib
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, IntegerType
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.feature import StringIndexer
from pyspark.ml import Pipeline
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBRegressor

spark = SparkSession.builder.appName("BigSale").getOrCreate()

kafka_config = {
        "bootstrap_servers": 'localhost:9092',
        "value_deserializer": lambda v: json.loads(v.decode("utf-8")),
    }

KAFKA_TOPIC_NAME_CONS = "BigSale_test"

schema = StructType([
    StructField("Item_Identifier", StringType(), True),
    StructField("Item_Weight", DoubleType(), True),
    StructField("Item_Fat_Content", StringType(), True),
    StructField("Item_Type", StringType(), True),
    StructField("Item_MRP", DoubleType(), True),
    StructField("Outlet_Identifier", StringType(), True),
    StructField("Outlet_Establishment_Year", IntegerType(), True),
    StructField("Outlet_Size", StringType(), True),
    StructField("Outlet_Location_Type", StringType(), True),
    StructField("Outlet_Type", StringType(), True),
])

def predict(data): 
    print(data )
    preproccessed_data = preprocess(data)
    loaded_regressor = joblib.load('./xgb_regressor_model.joblib')
    result = loaded_regressor.predict(preproccessed_data)
    return result

def preprocess(received_data): 
    big_mart_data = pd.DataFrame([received_data])
    for column in big_mart_data.columns:
        if(big_mart_data[column].dtype=='object'):
            encoder=LabelEncoder() 
            big_mart_data[column]=encoder.fit_transform(big_mart_data[column])
    return big_mart_data.values

if __name__ == "__main__":
    message_dict= {'Item_Identifier': 'FDP46', 
                   'Item_Weight': None, 
                   'Item_Fat_Content': 'Low Fat', 
                   'Item_Visibility': "no", 	
                   'Item_Type': 'Snack Foods', 
                   'Item_MRP': 91.083, 
                   'Outlet_Identifier': 'OUT027', 
                   'Outlet_Establishment_Year': 1985, 
                   'Outlet_Size': 'Medium', 
                   'Outlet_Location_Type': 'Tier 3',
                    'Outlet_Type': 'Supermarket Type3'}
    print("result ", predict(message_dict))