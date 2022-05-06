#json
import json
a={"b":"vanshiak","c":"anything","f":404}
print(type(a))
# load(): This method is used to load data from a JSON file into a python dictionary.
# Loads( ): This method is used to load data from a JSON variable into a python dictionary.
# dump(): This method is used to load data from the python dictionary to the JSON file.
# dumps(): This method is used to load data from the python dictionary to the JSON variable.
b=json.dumps(a)
print(type(b))
data='{"var1":"harry", "var2":56}'
parsed=json.loads(data)
print(parsed)
data2 = {
    "channel_name": "CodeWithHarry",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('roti', 540),
    "isbad": False
}
c=json.dumps(data2)
print(c)


