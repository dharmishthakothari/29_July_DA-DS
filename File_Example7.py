import json
with open('student_data.json',"a") as f:
    std_data={
        "name":"Khushali",
        "surname":"maheta",
        "address":"C G Road",
        "c_no" : 23455456
    }
    json.dump(std_data,f)
    print("Data Written successfully ")