try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
except:
    print("Some error occurred")
finally:
    print("I am always executed")

def func1():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the index: "))
        print(l[i])
        # return 1
    except:
        print("Some error occurred")
        # return 0
    finally:
        print("I am always executed")

print('I am executed after finally because return statement is commented out')

x = func1()
print(x)