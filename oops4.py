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

harry = Employee("harry",5000,"Manager")
rohan = Employee("rohan",3500,"assistant manager")

rohan.change_leaves(4)     # not taking self as input
# Employee.no_of_leaves = 56
print(harry.no_of_leaves)

