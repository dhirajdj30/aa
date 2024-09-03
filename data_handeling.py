from turtle import update
from databse import collection
def insert_data_base(data):
     update_data={}
     update_data["pid"]=data["pid"]
     update_data["itemId"]=data["itemId"]
     update_data["brand"]=data["brand"]
     update_data["title"]=data["title"]
     update_data["mrp"]=data["mrp"]
     update_data["price"]=data["price"]
     update_data["specialPrice"]=data["specialPrice"]

     update_data["rating"]=data["rating"]
     update_data["variants"]=data["variants"]
     update_data["highlights"]=data["highlights"]
     update_data["description"]=data["description"]
     qna_list=[]
     for qna in data["qna"]:
          del qna["answered_by"]
          del qna["type"]
          del qna["upvotes"]
          del qna["downvotes"]
          qna_list.append(qna)

     update_data["qna"]=qna_list

     update_data["features"]=data["features"]
     update_data["specifications"]=data["specifications"]
     update_data["manufacturingPackagingImport"]=data["manufacturingPackagingImport"]


     


     collection.insert_one(update_data) 







