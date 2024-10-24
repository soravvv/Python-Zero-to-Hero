# Dictionaries are ordered
ep1 = {1013: 90, 123: 89, 546: 69, 670: 45}
ep2 = {222: 67, 566: 900}

ep1.update(ep2)
print(ep1)

# ep1.clear()
# print(ep1)

ep1.pop(123) # just takes the key name and it will remove that element
print(ep1)

ep1.popitem() # it simply removes the item from the last of dictionary
print(ep1)

# del ep1 # it will delete the dictionary
# print(ep1)

del ep1[546]
print(ep1)