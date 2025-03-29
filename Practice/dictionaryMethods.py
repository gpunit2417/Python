dict1 = {"Name": "Punit", "Age": 20, "City": "Hisar"}

# print(dict1["City"])
# print(dict1.get("Name"))

# print(dict1.get("rollno"))  #key absent, returns None 
# print(dict1["rollno"])        #key absent, return KeyError

print(dict1.keys())
#output: dict_keys(['Name', 'Age', 'City'])

print(dict1.values())
#output: dict_values(['Punit', 20, 'Hisar'])

print(dict1.items())
#output: dict_items([('Name', 'Punit'), ('Age', 20), ('City', 'Hisar')])