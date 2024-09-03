import http.client
import json
from data_handeling import insert_data_base
def import_data(pid):
    conn = http.client.HTTPSConnection("real-time-flipkart-api.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "61e0d2f218mshd742ffb7677821fp1e3fd5jsn1adb059f4ec8",
        'x-rapidapi-host': "real-time-flipkart-api.p.rapidapi.com"
    }
    #pid="ACCGXX62ATGFSZG8"
    conn.request("GET", f"/product-details?pid={pid}", headers=headers)

    res = conn.getresponse()
    data = res.read()

    # Decode bytes to string
    data_str = data.decode("utf-8")

    # Parse JSON string into a Python object
    json_object = json.loads(data_str)
    
    
    # Print the JSON object (for debugging)
    #print(json.dumps(json_object, indent=4))
    
    # Write JSON to a file
    with open(f"pid_data/{pid}.json", "w") as outfile:
        json.dump(json_object, outfile, indent=4)

    insert_data_base(data=json_object)
