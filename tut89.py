a = input("What is your name ")
b = input("How much do you earn ")
# if int(b)==0:
#     raise ZeroDivisionError("Your earning is zero ")

# if a.isnumeric():
#     raise Exception("Numbers are not allowed")

# print(f"Hello {a}")
# 1000lines taknig 1 hour

c = input()

try:
    print(a)

except Exception as e:
    if b == "harry":
        raise ValueError("Harry is blocked he is not allowed ")

    print("Exception handled")
