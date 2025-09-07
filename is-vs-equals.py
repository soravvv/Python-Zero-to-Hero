a = 4
b = "4"

print(a is b) # it compares exact location of object in memory
print(a == b) # it compares value

c = 3
d = 3
print(a is b) # true
print(a == b) # true
# because python will not create another memory location for 3 because 3 is already there so python will use that only. Also c and d are constant which means python thinks that these values are not going to change because its constant. In tuple the o/p would be same. But in list the o/p would be different

e = (1, 2)
f = (1, 2)
print(e is f) # true
print(e == f) # true


g = [1, 2]
h = [1, 2]
print(g is h) # false
print(g == h) # true