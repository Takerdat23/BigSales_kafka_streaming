import pandas as pd
from kafka import KafkaProducer
from datetime import datetime
import time
import random
import numpy as np
import json

# pip install kafka-python

KAFKA_TOPIC_NAME_CONS = "BigSale_test"
KAFKA_BOOTSTRAP_SERVERS_CONS = 'localhost:9092'
kafka_producer_obj = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS_CONS)
if __name__ == "__main__":
    print("Kafka Producer Application Started ... ")

    
    
    filepath = "Test.csv"
   
    data_df = pd.read_csv(filepath)
    data_dict = data_df.to_dict(orient="records")
    
    message_list = []
    message = None
    for message in data_dict:
        message_fields_value_list = {}

        message_fields_value_list["Item_Identifier"] = message["Item_Identifier"]
        message_fields_value_list["Item_Weight"] = message["Item_Weight"]
        message_fields_value_list['Item_Visibility'] = message['Item_Visibility']
        message_fields_value_list["Item_Fat_Content"] = message["Item_Fat_Content"]
        message_fields_value_list["Item_Type"] = message["Item_Type"]
        message_fields_value_list["Item_MRP"] = message["Item_MRP"]
        message_fields_value_list["Outlet_Identifier"] = message["Outlet_Identifier"]
        message_fields_value_list["Outlet_Establishment_Year"] = message["Outlet_Establishment_Year"]
        message_fields_value_list["Outlet_Size"] = message["Outlet_Size"]
        message_fields_value_list["Outlet_Location_Type"] = message["Outlet_Location_Type"]
        message_fields_value_list["Item_Identifier"] = message["Item_Identifier"]
        message_fields_value_list["Outlet_Type"] = message["Outlet_Type"]

        json_message = json.dumps(message_fields_value_list)

        print("Message Type: ", type(json_message))
        print("Message: ", json_message)
       
        kafka_producer_obj.send(KAFKA_TOPIC_NAME_CONS, json_message.encode('utf-8'))
        time.sleep(1)

    print("Kafka Producer Application Completed. ")