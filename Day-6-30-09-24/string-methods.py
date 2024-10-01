# Strings are immutable which means we cannot change strings
a = "Sorav"
print(len(a))
print(a.upper())
print(a.lower())

strip = "!!!Sorav!!!!!!!"
print(strip.rstrip("!")) # it will remove all the exclamatory signs after my name, but it does not remove the signs before my name

print(a.replace("Sorav", "Ankush")) # it will replace my name with ankush

split = "Sorav Ankush Viswajeet Surya"
print(split.split(" "))

blog_heading = "introduction to python"
print(blog_heading.capitalize()) # it capitalize first character of first word and it will make every other letter lowercase.

str1 = "Welcome to the tech"
print(len(str1))
print(str1.center(50)) # it will add extra spaces before my sentence

print(split.count("a")) # it will count the occurences of a

str2 = "Welcome to the console !!!"
print(str2.endswith("!")) # it will check if my string is ending with given value or not

find = "He's name is sorav. He is an honest man in a country, 1234"
print(find.find("is")) # it will find the first occurence of given input value and after finding a value it will return the index else it will return -1.

print(find.index("is")) # if we are sure that a thing will be available in our string or an array then we will use that index and in case if index not able to find that value then it will give an error

# if we want to know that our string contains alpha numeric values or not then we will use it, it returns a boolean value
print(find.isalnum())

# can use islower() to check if our string is in lower case or not

# isprintable() 

# isspace() if our string is containing white spaces, it returns boolean

# istitle() it checks if each word in the string has capital character or not, it returns boolean

# swapcase() it make uppercase to lowercase and vice versa

# title() it will make every character of a word capital