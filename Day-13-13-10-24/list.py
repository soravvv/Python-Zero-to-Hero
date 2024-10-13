marks = [3, 5, 6, "Sorav", 4, 7, 8, 9, 10, 1]
print(marks)
print(type(marks))
# print(marks[-1])

if 7 in marks:
    print("YES")
else:
    print("NO")

if "Sorav" in marks:
    print("YES")
else:
    print("NO")

if "ra" in "Sorav":
    print("YES")
else:
    print("NO")

print(marks[:]) # it will print the list
print(marks[1:8]) # it will print from 1 to 7
print(marks[1:8:2]) # it will print from 1 to 7 but it will jump index by 2 because we have mentioned it in the end

lst = [i for i in range(5) if i % 2 == 0]
print(lst)