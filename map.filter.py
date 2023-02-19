numbers = ["3", "34", "64"]
numbers = list(map(int, numbers))
print(numbers)
print(type(numbers))

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

# numbers[2] = numbers[2] + 1
# print(numbers[2])

num = [2,3,4,5,6,75,22,43,2]
square = list(map(lambda( x: x*x)))