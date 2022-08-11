class Employee:
    no_of_leaves = 8
    var = 8
    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"Name is {self.name} salary is {self.salary} and role is {self.role}."

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)

class player:
    var = 9
    no_of_games = 4
    def __init__(self,name,game):
        self.name = name
        self.game = game
    def printdetails(self):
        return f"The Name is {self.name}. Game is {self.game}"

class coolprogrammer(Employee, player):
#    var = 10
    language = "c++"
    def printlanguage(self):
        print(self.language)

harry = Employee("harry", 5000, "Manager")
rohan = Employee("rohan", 3500, "assistant manager")

shubham = player("shubham",["cricket"])
karan = coolprogrammer("karan",100000,"coolprogrammer")
print(karan.printdetails())
karan.printlanguage()
print(karan.var)