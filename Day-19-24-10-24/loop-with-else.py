for i in range(5):
    print(i)
else :
    print("Sorry no i")

# else does not work with break
for i in range(5):
    print(i)
    if i == 4:
        break
else :
    print("Sorry no i-")
print("Out of loop")