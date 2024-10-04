num = int(input("Enter the value of num: "))
if(num < 0):
    print("Number is negative")
elif(num == 0) :
    print("Number is zero")
elif(num == 999) :
        print("Number is special")
else :
    print("Numver is positive")
    print("testing")

print("I am happy now")

# Exercise- Greet according to timezone
import time
timestamp = time.strftime('%H:%M:S')
print(timestamp)
hour = time.strftime('%H')
print(hour)
second = time.strftime('%S')
print(second)

if(int(hour) < 12):
     print('Good Morning!')
elif (int(hour) < 16) :
    print('Good Afternoon!')
elif (int(hour) < 20) :
    print('Good Evening')
else :
     print('Good Night!')