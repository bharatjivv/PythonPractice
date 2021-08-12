# Global And Local Variables
"""
l = 10 # Global Variable
def function1(n):
    # l = 5   # Local Variable
    m = 8   # Local Variable
    global l
    l = l + 45
    print(l, m)
    print(n, "I have printed")

function1("This is me")
"""


x = 89
print("Program has started")
def harry():
    x = 20
def rohan():
    global x
    x = 88

print("before calling rohan()", x)
rohan()
print("after calling rohan()", x)
harry()