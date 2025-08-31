f = open('myfile.txt', 'r')
# f = open('myfile.txt')  # default is read mode
# f = open('myfile.txt', 'w') # write mode, if file does not exist in write mode then that file will be created newly
text = f.read()
print(text)
f.close()

f = open('myfile.txt', 'w')
f.write("Hello, Sorav here")
f.close()

f = open('myfile.txt', 'a') # appending
f.write("How are you doing?")
f.close()

with open('myfile.txt', 'a') as f:
    f.write("Hey, I am inside with") # using with keyword we dont need to close the file

with open('myfile.txt', 'r') as f:
    print(type(f))
    f.truncate(5)


# Move to the 10th byte in the file
# f.seek(10)


data = f.read(5)
print(data)