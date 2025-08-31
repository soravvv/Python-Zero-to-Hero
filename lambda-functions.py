def double(x):
    return x*2

print(double(5))

double = lambda x: x*2
cube = lambda x: x*x*x
avg = lambda x,y,z: (x + y + z) / 3

print(double(2))
print(cube(5))
print(avg(3, 5, 10))

def appl(fn, value):
    return 6 + fn(value)

print(appl(lambda x: x * x, 2))