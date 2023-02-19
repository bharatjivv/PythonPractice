"""
# Factorial using iterative approach 
def factorial(n):
    fac = 1
    for i in range(n):
        fac = fac * (i + 1)
    return fac 

number = int(input("Enter a number "))

print("The factorial of the number is ", factorial(number))

# Factorial using recursive method

def factorial_recursive(n):
    if n == 1: 
        return 1
    else: 
        return n * factorial_recursive(n-1) 

"""

# Lambda functions or anonymous functions
# def add(a, b):
#     return a+b

# minus = lambda x, y: x-y

# # def minus(x, y):
# #     return x-y

# print(minus(9, 4))

def a_first(a):
    return a[0]

a =[[11, 34], [5, 56], [8,23]]
a.sort(key=a_first)
print(a)