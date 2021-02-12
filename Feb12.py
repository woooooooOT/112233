import random

print('My favourite book is \"Magic Treehouse\"\nand \nMy favourite character is this: \"\\\" the backward slash ')

print (random.randint(1,999))

for x in range(0,10):
    print (x)#for(int n, n<10, n++){}

x = int(2.5e4)
print (x)

y = "apple"
print (y.upper())
print (y.center(15,"-"))

address = "1460 Devon Rd"
city = "Oakville"
postal = "L6J 3L6"
print(address.center(70) + '\n' + city.center(70) + '\n' + postal.center(70))

string = "apple Apple apple apple appleapple"
print(string.count("apple"))  # retuens 5

a = 5
if 1 <= a <= 10:  # can compare multiple at the same time
    # SAME AS if 1<=x and x<= 10
    print("x is between 1 and 10")

string1 = "ha"
if string1 in "happy":
    print("trueeeeeeee")
