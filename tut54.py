class Employee:
    no_of_leaves = 8
    pass

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 45
rohan.role = "Student"

print(harry.salary)
print(Employee.no_of_leaves)
rohan.no_of_leaves = 9
print(rohan.no_of_leaves)
print(Employee.no_of_leaves)
print(rohan.__dict__)