

import json



with open("sample1.json","r") as f:  #will open the json and then print data in terminal in single string
    contents = f.read()
print(contents)
   
data= {
    "name": "John Smith",
    "age": 35,
    "is_student": False
}
with open("sample1.json", "w") as f:
    json.dump(data, f)

test_dict = {  #to transform a dictionary to a json file
    "name" : "Lou",
    "age" : 7,
    "city" : "London"
}

with open("newjson.json", "w") as f:
    json.dump(test_dict, f)

with open("sample1.json") as f:  #will open the json and then print data in terminal in python object
    data =json.load(f)
print(data)t