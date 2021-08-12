# Self and init constructors
class Employee:
    no_of_leaves = 8
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role


    def printDetails(self):
        return f"Name is {self.name}. Salary is {self.salary}k and role is {self.role}"


harry = Employee("harry", 455, "Instructor")
# rohan = Employee()

# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"

# rohan.name = "Rohan"
# rohan.salary = 45
# rohan.role = "Student"

# print(rohan.printDetails())

# print(rohan.no_of_leaves)

print(harry.name)