# Python docstrings are the string literals that appear right after the definition of a function, emthond, class, or module. Docstring should be written just after the function declaration else it will not work.

def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)