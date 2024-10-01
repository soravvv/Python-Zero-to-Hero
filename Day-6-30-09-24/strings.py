names = "Sorav,Ankush,Viswajeet"
print(len(names)) # finding length
print(names[0:5]) # splicing
print(names[:5]) # if I will not write 0 then the python will automatically consider it as 0
print(names[0:-3]) # -3 means the total length of our names character -3 which means 22 - 3 = 19 so python will print the output from 0 to 19. print(names[0:len(names)-3])

# Quick Quiz:
nm = "Sorav"
print(nm[-4:-2]) # solve it without running it