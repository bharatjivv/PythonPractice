# Recursions in Python
# def print2(str1):
#     print2(str1)
#     print("This is " + str1)
# print2("harry")

def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

def factorial_recursive(n):
    if n ==1:
        return 1
    else:
        return n * factorial_recursive(n-1)


number = int(input("Enter the number : "))
print("Factorial using iterative method", factorial_iterative(number))
print("Factorial using recursive method", factorial_recursive(number))

# 0 1 1 2 3 5 8 13
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else: 
        return fibonacci(n-1) + fibonacci(n-2)


print("Fibonacci of numbers", fibonacci(number))