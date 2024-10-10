for i in range(12):
    print("5 X", i+1, "=", 5*(i+1))
    if(i == 10):
        break

print("Loop breaked")

for i in range(12):
    if(i+1 == 10):
        print("Skipped the iteration at 10")
        continue
    print("5 X", i+1, "=", 5*(i+1))

i = 0
while True:
    print(i)
    i = i + 1
    if(i%100 == 0):
        break

