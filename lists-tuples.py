# Lists 
names = ["Sorav", "Ankush", "Deepanshu", "Aman", "Surya", "Viswajeet", "Farazu", "Akash", "Shivangi"]
for i in range(len(names)):
    print(names[i])

for i in range(len(names)):
    name = names[i]
    print(name)

for i in range(len(names)):
    name = names[i]
    if(name == "Shivangi"):
        print("true")
    else:
        print("false")

names.append("Subash")
print(names)

names.remove("Farazu")
print(names)

names.reverse()
print(names)

# List Comprehension
integers = [i for i in range(10)]
print(integers)

evenNum = [i for i in range(20) if i % 2 == 0]
print(evenNum)

oddNum = [i for i in range(20) if i % 2 == 0]
print(oddNum)

# Tuples -> Cannot change anything in tuples (Immutable)
tup = (1, 2, 3, 4, 5, 6, 7)
print(type(tup), tup)

for i in range(len(tup)):
    print(i, '->', tup[i])

if(5 in tup):
    print("Yes")