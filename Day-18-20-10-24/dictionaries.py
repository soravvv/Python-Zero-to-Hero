# Dictionary is combination of key value pair
dic = {
    "Sorav": "Human being",
    "Spoon": "Object",
    344: "Sorav",
    76: 'Ankush',
    98: "rahul",
    12: "Surya"
}
print(dic["Sorav"])
print(dic[344])
print(dic.get(98))

for key in dic.keys():
    print(f"The value corresponding to the key {key} is {dic[key]}")

print(dic.values())
print(dic.items()) # it will return key value pairs

for key, value in dic.items():
     print(f"The value corresponding to the key {key} is {value}")