# This script will show basics for For loop in python
for i in range(1, 10, 2):  # Range function will take input of start, end and interval. We can use also _ if variable
    # is not used code
    print(i, "Hello")
else:
    print("Loop Ended")

# Below iterative for loops will print math tables from 1 to 10
x = range(1, 11)
for i in x:
    print("num = ", i, ":", end=" ")
    for j in x:
        print("{:2d}".format(i * j), end=" ")
    print(" ")
# Break statement in for Loop for wrong password detection 3 times
for i in range(3):
    password = str(input("Enter your password: "))
    if password == "secret":
        print("Correct Password")
        break
    else:
        print("You have 3 attempts")
# Pass and Break uses in Loop
mystr = input("Input a string: ")
digits = 0
letters = 0
for i in mystr:
    if i.isdigit():
        digits += 1
    elif i.isalpha():
        letters += 1
    else:
        pass  # Nothing will execute in case of pass function here
print("Digits: ", digits)
print("Letters: ", letters)
# Comprehensions in Python: Take first letter of each element from list and make all upper with condition
list1 = ["My", "Name", "is", "Teche", "coder"]
items = [word[0].upper() for word in list1 if word != "coder"]
print(items)
# select vowels from the word in one line of code
item2 = [i for i in input(" Type any word: ").lower() if i in ["a", "e", "i", "o", "u"]]
print(item2)
# comprehensions with nested for loops
stationery = ["Pen", "marker", "Ink"]
colors = ["Red", "Blue", "Black"]
combined = [(i,j) for j in stationery for i in colors]
print(combined)
