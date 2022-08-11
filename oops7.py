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

class programmer(Employee):
    no_of_holidays = 70
    def __init__(self,name,salary,role,languages):
        self.name = name
        self.salary = salary
        self.role = role
        self.languages = languages

    def printprog(self):
        return f"Programmer's Name is {self.name} salary is {self.salary} and role is {self.role} The languages are {self.languages}"

harry = Employee("harry", 5000, "Manager")
rohan = Employee("rohan", 3500, "assistant manager")

shubham = programmer("shubham", 555,"programmer",["python"])
karan = programmer("karan",7000,"programmer",["python","java"])
print(karan.no_of_holidays)