def average(a, b):
    print("The average is ", (a+b)/2)

average(4, 6)

def name(fname, mname = "Sorav", lname = "Malviya"):
    print("Hello, ", fname, mname, lname)

name('Amy', 'Agarwal')

def averageNumbers(*numbers):
    # print(type(numbers)) <class 'tuple'>
    sum = 0
    for i in numbers:
        sum = sum + i
        print("Average is:", sum / len(numbers))

averageNumbers(5, 6)

def name(**name):
    # print(type(name)) <class 'dict'>
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname="Sorav", lname="Malviya", fname="Sorav Malviya")
