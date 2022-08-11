class Employee:
    no_of_leaves = 8

    def __init__(self, name1, salary1, role1):
        self.name = name1
        self.salary = salary1
        self.role = role1

    def printdetails(self):
        return f"The name is {self.name} and salary is {self.salary} thus the role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):                               # mapping operators to functions
        return self.salary+other.salary

    def __truediv__(self, other):                            # mapping operators to functions
        return self.salary/other.salary

    def __repr__(self):
        return f"Employee ('{self.name}', {self.salary}, '{self.role}')"
    def __str__(self):
        return self.printdetails()
emp1 = Employee("harry",3456,"programmer")
# emp2 = Employee("jerry",356,"guard")
print(repr(emp1))                # it will fiest give preference to str if not mention