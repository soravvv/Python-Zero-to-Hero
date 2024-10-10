# a = 9
# b = 8
# geometricMean = (a*b)/(a+b)
# print(geometricMean)

# c = 8
# d = 7
# geometricMean2 = (a*b)/(a+b)
# print(geometricMean2)

def calculateGeomentricMean(a, b): # def= user defined function
    if(a > b):
        print("a is greater")
    else:
        print("b number is greater or both numbers are equal")
    mean = (a*b)/(a+b)
    print(mean)

calculateGeomentricMean(7, 8)

def noBodyFunction(a, b):
    pass