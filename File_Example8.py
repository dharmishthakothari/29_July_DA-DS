import json
with open('student_data.json',"r") as f:
    std_data=json.load(f)
    print(std_data)  
    print(std_data['name'])  