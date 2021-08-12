# print("For each loops")

# for x in range(1, 11):
#     print(x)

# for x in range(10, -11, -1):
#     print(x)

# for x in range(-1, -10, -1):
#     print(x)

# n = int(input("Enter a number \n"))

# for x in range(10, 0, -1):
#     print("%d X %d = %d"%(n,x,n*x))

# x = 1

# while x < 10:
#     print(x)
#     x = x + 1

import random 
from PIL import Image

def dice():
    x = random.randint(1,6)
    print("Testing Dice Function ")
    print(x)
    
    if x == 1:
        im = Image.open("1.jpeg")
    elif x == 2:
        im = Image.open("2.jpeg")
    elif x == 3:
        im = Image.open("3.jpeg")
    elif x == 4:
        im = Image.open("4.jpeg")
    elif x == 5:
        im = Image.open("5.jpeg")
    elif x == 6:
        im = Image.open("6.jpeg")
    im.show()

dice();