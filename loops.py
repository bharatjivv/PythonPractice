# fruits = ["apples", "oranges", "mangoes"]
# for i in fruits:
#     print(i)

# fruits = ["apples", "oranges", "mangoes"]
# for i in fruits:
#     str_length = 0
#     for j in i:
#         str_length += 1
#     print(f"The name of fruit is {i} and its length is {str_length}")

# fruits = ["apples", "oranges", "mangoes"]
# for index, fruit in enumerate(fruits):
#     print(f"{index + 1}. {fruit} ")

for i in range(1, 3):
    for j in range(1, 3):
        print(f"{i} * {j} = {i*j}")