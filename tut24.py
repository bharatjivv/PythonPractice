# Try catch exception handling
# Except Exception Handling In Python

print("Enter num1 ")
num1 = input()
print("Enter num2 ")
num2 = input() 

try:
    print("The sum is : ", 
        int(num1) + int(num2))
except Exception as e:
    print(e)

print("This line is  very important")

# 'as' keyword will be discussed later