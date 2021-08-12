a = 9
b = 8
# c = sum((a, b)) # built-in function

def function1(a, b):
    print("Hello You are in function ", a+b)

# function1()
# print(function1())
# function1(5, 7)

def function2(a, b):
    """This is a function which will calculate average of two numbers"""
    average = (a+b)/2
    # print(average)
    return average

# function2(5, 7)
v = function2(5, 7)
print(v)

print(function2.__doc__)    # This is a doc string 