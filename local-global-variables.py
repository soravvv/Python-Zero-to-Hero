x = 4
print(x)

def hello():
    global x # after using this global keyword the actual x value will start getting updating
    x = 6
    print(x)
    print("Hello Sorav")