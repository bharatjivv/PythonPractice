import math
# F strings 
me = "harry"
a1 = 3
# a = "this is %s %s"%(me, a1)
# print(a)
# a = "This is {1} {0}"
# b = a.format(me, a1)
# print(b)

a = f"This is {me} {a1} {40*2} {math.cos(65)}"
print(a)