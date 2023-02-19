# var = 0
# while var < 6:
#     var += 1
#     if var % 2 == 0 :
#         continue
#     print("#")



# my_list = [1,2,3,4]
# print(my_list[-3:-2])

# Doubt
# i = 0 
# while i <= 5:
#     i += 1
#     if i % 2 == 0:
#         break
#     print("#")
    
    
# var = 1
# while var < 10:
#     print("#")
#     var = var << 1



# for i in range(1):
#     print("#")
# else:
#     print("%")


# a = 1
# b = 0
# c = a & b
# d = a | b
# e = a ^ b

# print(c + d + e)


# my_list = [[0,1,2,3] for i in range(2)]
# print(my_list[2][0])



# t = [[3-i for i in range (3)] for j in range (3)]
# s = 0
# for i in range(3):
#     s += t[i][i]
# print(s)





# def is_year_leap(year):
#     if year % 4 == 0:
#         return True
#     elif year % 100 == 0:
#         return True
#     else : return False

# def days_in_month(year, month):
#     if month in {1,3,5,7,8,10,12}:
#         return 31
    
#     elif month==2:
#         if is_year_leap(year):
#             return 29
#         else: return 28
#     elif month in {4,6,8,9,11}:
#         return 30
#     else:
#         return none


# test_years = [1900, 2000, 2016, 1987]
# test_months = [2, 2, 1, 11]
# test_results = [28, 29, 31, 30]
# for i in range(len(test_years)):
# 	yr = test_years[i]
# 	mo = test_months[i]
# 	print(yr, mo, "->", end="")
# 	result = days_in_month(yr, mo)
# 	if result == test_results[i]:
# 		print("OK")
# 	else:
# 		print("Failed")



# def is_year_leap(year):
#     if year % 4 == 0:
#         return True
#     elif year % 100 == 0:
#         return True
#     else : return False

# def days_in_month(year, month):
#     if month in {1,3,5,7,8,10,12}:
#         return 31
    
#     elif month==2:
#         if is_year_leap(year):
#             return 29
#         else: return 28
#     elif month in {4,6,8,9,11}:
#         return 30
#     else:
#         return none

# def day_of_year(year, month, day):


# print(day_of_year(2000, 12, 31))

# x = 1 // 5 + 1 / 5
# print(x)

# lst = [i for i in range(-1, -2)]
# for i in range():
#     print(lst[i])

# my_list = [x * x for x in range(5)]

# def fun(lst):
#     del lst[lst[2]]
#     return lst

# print(fun(my_list))

# print(hello, world!)

# tup = (1,2,4,8)
# tup = tup[-2:-1]
# tup = tup[-1]
# print(tup)

# det = {}
# det ['1'] = (1,2)
# det['2'] = (2,1)

# for x in det.keys():
#     print(det[x][1], end="")
    
    
# dd = {"1":"0", "0":"1"}
# for x in dd.vals():
#     print(x, end="")

# value = input("Enter val : ")
# print(int(value)/len(value))
# print(len(value))

# foo = (1,2,3)
# foo.index(0)

# lst = [[x for x in range(3)] for y in range(3)]

# for r in range(3):
#     for o in range(3):
#         if lst[r][o] % 2 != 0:
#             print("#")

# my_list = [1, 2]
# for v in range(2):
#     my_list.insert(-1, my_list[v])
# print(my_list)

# a = 1 
# b = 1

# a = a ^ b
# print(a)

# print("a", "b", "c", sep= "^")


# def fun(i=2, o = 3):
#     return i * o

# print(fun(o=2))


# def func(x, y):
#     if x == y:
#         return x
#     else: 
#         return fun(x, y-1)



# print(fun(0,3))

# det = {'one': 'two', 'three': 'one', 'two':'three'}
# v = det['three']

# for k in range(len(det)):
#     v = det[v]

# print(det[v])
# x = 1 % 2
# print(x)


# z = 0
# y = 10
# x = y < z and z > y or y > z and z < y
# print(x)

# x = int(input())
# y = int(input())
# x = x%y
# x = x%y
# y = y%x 
# print(y)

# def fun(x):
#     if x % 2 ==0:
#         return 1
#     else:
#         return 
    
# print(fun(fun(2)) + 1)

# my_tuple = (1, 2, 3, 4)
# my_tuple[1] = my_tuple[1] + my_tuple[0]

# def fun(x, y, z):
#     return x + 2 * y + 3 * z

# print(fun(0, z=1, y=3))


# def fun(x):
#     x += 1
#     return x 

# x = 2
# x = fun(x + 1)
# print(x)

# def any():
#     print(var + 1, end='')

# var = 1
# any()
# print(var)

# tup = (1,2,4,8)
# tup = tup[1:-1]
# tup = tup[0]
# print(tup)


# x = 1 
# y = 2
# x, y, z = x, x, y
# z, y, z = x, y, z

# print("second")
# print(x, y, z)

# def func(a, b):
#     return b ** zip

# print(func(b=2, 2))

# x = 2 % 1 
# print(x)

# foo = (1,2,3)
# foo.index(0)