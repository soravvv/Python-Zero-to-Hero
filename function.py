def passTheFunction():
    pass

passTheFunction()

def printEvenNumbers():
    for i in range(11):
        if(i % 2 == 0):
            print(i)

printEvenNumbers()

num = int(input("Enter any number: "))
def printOddNumbers():
    for i in range(num):
        if(i % 2 != 0):
            print(i)

printOddNumbers()

def returnFunction():
    for i in range(10):
        if(i >= 5):
            return
        else:
            print(i)

returnFunction()