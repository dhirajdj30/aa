from flask import Flask,request
from import_data_api import import_data
app = Flask(__name__)

from databse import collection

@app.route("/pagal",methods=['GET','POST'])
def hello_world():
    if request.method=="GET":
            pid=request.args.get('pid')
            pid_obj= collection.find_one({"pid":pid})
            pid_objs=collection.find()
            sum = 0
            for i in pid_objs:
                sum+=1
                print(i)
            print(sum)
            if not pid_obj:
                import_data(pid=pid)
                return "<p>Hello, World!</p>"
            return "<p>present!</p>"

           # initial=int(request.args.get("initial"))
    if request.method == 'POST':
        required_fields= ["financial_id","amount","reference_number","note","payment_mode","firm_name","source","status"]
        request_data = request.get_json()
       # missing_fields={key: error_data[key] for key in required_fields if not request_data.get(key)}
        

if __name__ == '__main__':
    app.run(debug=True)