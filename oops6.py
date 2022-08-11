class Employee:
    no_of_leaves = 8
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

harry = Employee("harry", 5000, "Manager")
rohan = Employee("rohan", 3500, "assistant manager")
karan = Employee.from_dash("karan-2500-student")

Employee.printgood("Harry")
# rohan.change_leaves(20)     # not taking self as input
# Employee.no_of_leaves = 56
# print(harry.no_of_leaves)

