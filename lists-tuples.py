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



# Tuple practice questions
# Create a tuple named fruits that contains "apple", "banana", and "cherry".
# Print the second item in the tuple.
fruits = ("Apple", "Banana", "Cherry")
print(fruits[1])

# Check if the value "banana" exists in the tuple fruits. Print a message if it does.
if("Banana" in fruits):
    print("Yes banana exist in fruits tuple using if condition only")

for i in fruits:
    if("Banana" in fruits):
       print("Yes banana exist in fruits tuple using loop") 
       break

# Concatenate two tuples
# and store the result in a new tuple.
t1 = (1, 2, 3)
t2 = (4, 5)
newTuple = t1 + t2
print(newTuple)

# Write a function that takes a tuple of integers and returns a tuple with only the even numbers.
def evenIntegers(integers):
    evenTuples = ()
    if(integers):
        for i in integers:
            if(i % 2 == 0):
                evenTuples = evenTuples + (i,)
    return evenTuples

print(evenIntegers((1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 22)))

# Given a tuple of nested tuples, Flatten it into a single tuple like (1, 2, 3, 4, 5, 6).
nested = ((1, 2), (3, 4), (5, 6))
flat = ()
for inner in nested:
    for item in inner:
        flat += (item,)

print(flat)

# Optimized way
def flatten(t):
    ans = ()
    for i in t:
        if type(i) == tuple:
            ans += flatten(i)
        else:
            ans += (i,)
    return ans

print(flatten(nested))

# List practice questions
# Create a list of 5 integers. Replace the third element with a new value and print the list.
int = [1, 2, 4, 4, 5]
int[2] = 3
print(int)

# Add a new item at the end of a list using .append() and sort the list in descending order.
intList = [1, 2, 3, 4, 5, 6, 7, 10, 8, 17, 15, 12, 11, 18]
intList.append(19)
print(sorted(intList))
intList.sort()
print(intList)

# Write a function that takes a list and returns a new list with only unique elements (remove duplicates).
def removeDuplicates(list):
    uniqueList = []
    for i in list:
        if i not in uniqueList:
            uniqueList.append(i)
    return uniqueList

print(removeDuplicates([1, 2, 2, 3, 4, 4, 5, 1, 6, 6, 0]))

# Given a list of strings, sort it by the length of each string instead of alphabetical order.
strings = ["apple", "fig", "banana"]
sorted_strings = sorted(strings, key=len)
print(sorted_strings)

# Write a program to rotate a list to the right by k positions.
# Example: [1, 2, 3, 4, 5] rotated by 2 → [4, 5, 1, 2, 3]
def rotatedListByKTimes(list, k):
    left = 0
    right = len(list) - 1
    for i in range(k+1):
        while left <= right:
            temp = list[left]
            list[left] = list[right]
            list[right] = temp
            left += 1
            right -= 1
    return list

print(rotatedListByKTimes([1, 2, 3, 4, 5], 2))

# Write a Python program to remove duplicates from a list using a set.
# Expected Output: [1, 2, 3, 4, 5]
input = [1, 2, 2, 3, 4, 4, 5]
uniqueInt = []
seen = set()
for i in input:
    if i not in seen:
        uniqueInt.append(i)
        seen.add(i)

print(list(uniqueInt))

# Check if two sets have any elements in common.
# Input: {1, 2, 3}, {3, 4, 5}
# Expected Output: True (common element is 3)