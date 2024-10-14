l = [1, 2, 4, 8]
print(l)

l.append(7) # it will push the 7 in the end of the list
print(7)

l.sort() # sort
print(l)

l.reverse() # it will reverse my list
print(l)

print(l.index(7)) # it will return the index of the first occurence of that number in the list 

m = l
m[0] = 0
print(l) # above expression will change the list[0] value, for avoiding this use below code

n = l.copy()
n[0] = 9
print(l, n)

l.insert(1, 899) # at index 1 insert 899
print(l)

a = [600, 700, 300]
l.extend(a)
print(l)
