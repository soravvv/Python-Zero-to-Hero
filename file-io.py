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