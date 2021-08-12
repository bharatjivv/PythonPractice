# Multiple Inheritence In python
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

class Player:
    no_of_games = 4
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printDetails(self):
        return f"The Name of Player is {self.name} and sports is {self.game}"

class CoolProgrammer(Employee, Player):
    language = "C++"
    def printlanguage(self):
        print(self.language)

harry = Employee("harry", 455, "Instructor")
rohan = Employee("rohan", 45, "Student")

shubham = Player("Shubham", ["cricket"])
karan = CoolProgrammer("Karan", 3888, "coolProgrammer")
det = karan.printDetails()

print(det)
