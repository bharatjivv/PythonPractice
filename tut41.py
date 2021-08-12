# def function_name_print(a, b, c, d):
#     print(a, b, c, d)

# function_name_print("Harry", "Rohan", "SkillF", "Hammad", "Shivam")

def funargs(normal, *argsRohan, **kwargs):
    print(normal)
    for item in argsRohan:
        print(item)
    print("\nNow I would like to introduce some of our heroes")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")

har = ["Harry", "Rohan", "SkillF", "Hammad", "Shivam", "The programmer"]
normal = "This is a normal arguement and The students are : "

kw = {"Rohan":"monitor", "Harry":"Fitness Instructor", "The Programmer":"Coordinator"}

funargs(normal, *har, **kw)

