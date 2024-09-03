connection_string_host="mongodb+srv://dhirajdj30:Pass%40123@authcluster.1rfcv.mongodb.net/?retryWrites=true&w=majority&appName=authcluster"
data_base="data"
from pymongo import MongoClient 
client = MongoClient() 
client = MongoClient(connection_string_host)
data_base=client[data_base] 

collection=data_base["flipcart"]