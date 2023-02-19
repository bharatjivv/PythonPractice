l = 10

def function1(n):
    # l = 5
    global l
    l = l + 7
    print(n, "I have printed ")
    print(l)

def bharat():
    x = 20
    def rohan():
        global x
        x = 88
    print("Before calling rohan()", x)
    rohan()
    print("After calling rohan()", x)


# function1("This is me ")
# function1("This is also me ")
# print(l)
# function1("Err")
bharat()