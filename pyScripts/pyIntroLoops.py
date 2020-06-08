# This script will show basics for For loop in python
for i in range(1, 10,2):  # Range function will take input of start, end and interval. We can use also _ if variable is not used code
    print(i, "Hello")
else:
    print("Loop Ended")

# Below iterative for loops will print math tables from 1 to 10
x = range(1, 11)
for i in x:
    print("num = ", i, ":", end =" ")
    for j in x:
        print("{:2d}".format(i * j), end =" ")
    print(" ")
# Break statement in for Loop for wrong password detection 3 times
for i in range(3):
    password = str(input("Enter your password: "))
    if password == "secret":
        print("Correct Password")
        break
    else:
        print("You have 3 attempts")

