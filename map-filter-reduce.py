#MAP
# def cube(x):
#     return x*x*x

# print(cube(3))

from functools import reduce


l = [1, 2, 3, 4, 5, 6, 7]
# newl = list(map(cube, l))
newl = list(map(lambda x: x*x*x, l))
print(newl)

#FILTER
def filter_function(a):
    return a>2

secondL = list(filter(filter_function, l))
print(secondL)

#REDUCE
numbers = [1, 2, 3, 4, 5]

def mysum(x, y):
    return x+y

sum = reduce(mysum, numbers)
print(sum)