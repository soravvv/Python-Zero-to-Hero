tup = (1, 5, 6, 'red') # tuple is not changable like list
print(type(tup), tup)
print(tup[0])
print(tup[2])

if 6 in tup:
    print("YES")
else:
    print("NO")

print(tup.count(6)) # it will count how many time 6 is coming in my tuple
# Tuples are immutable

# changing tuple value in illegal way
countries = ("Spain", "USA", "Italy", "England", "Germany")
temp = list(countries)
temp.append("India")
countries = tuple(temp)
print(countries)
print(len(countries))