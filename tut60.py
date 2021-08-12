# Single Inheritence In Python
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
        return cls(*string.split("-"))

    @staticmethod
    def printGood(string):
        print("This is good " + string)
        return "Thenga"

class Programmer(Employee):
    def __init__(self, aname, asalary, arole, languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages

    def  printProg(self):
        return f"The Programmer's name is {self.name}. Salary is {self.salary}k and role is {self.role}. The languages are {self.languages} "
    

harry = Employee("harry", 455, "Instructor")
rohan = Employee("rohan", 45, "Student")
karan = Employee.from_dash("Karan-480-Student")
# print(karan.printGood("Harry"))

shubham = Programmer("Shubham", 555, "Pirogiramer", ["python"])
karan = Programmer("Karan", 777, "Pirogiramer", ["python"])
print(karan.printProg())