# list1 = [["harry", 1], ["larry",3], ["Carry",6], ["marie",8]]
# print(list1[0], list1[1])
# dict1 = dict(list1)
# print(dict1)
# for item, lolly in dict1.items():
#     print(item, "eats" ,lolly ,"lollypop in a day")
# for item in dict1:
#     print(item)

items = [int, float, "harry", 5, 3, 3, 22, 21, 64, 233, 23, 6]

for item in items:
    if str(item).isnumeric() and item>6:
        print(item)

