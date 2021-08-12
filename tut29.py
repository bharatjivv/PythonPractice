# Pattern printing
"""
input  = integer n 
Boolean = True or False
n = no of rows

True
* 
** 
***
****

False
****
***
**
*
"""

print("How many Row Do You want to print")
one = int(input())
print("Type one or zero")
two = int(input())
new = bool(two)
if new == True:
    for i in range(1, one+1):
        for j in range(1, i+1):
            print("*", end=" ")
        print()

elif new == False:
    for i in range(one, 0, -1):
        for j in range(one, 0, i+1):
            print("*", end="")
        print()