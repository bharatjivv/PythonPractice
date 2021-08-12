# Class Method As Alternative Constructors
class Employee:
    no_of_leaves = 8
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role


    def printDetails(self):
        return f"Name is {self.name}. Salary is {self.salary}k and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        # params = string.split("-")
        # print(type(params))
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))



harry = Employee("harry", 455, "Instructor")
rohan = Employee("rohan", 45, "Student")
karan = Employee.from_dash("Karan-480-Student")

harry.change_leaves(34)
# Employee.no_of_leaves = 89

# print(harry.no_of_leaves)
print(karan.name)
print(karan.salary)
print(karan.role)