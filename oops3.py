class Employee:
    no_of_leaves = 8
    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"Name is {self.name} salary is {self.salary} and role is {self.role}."

harry = Employee("harry",5000,"Manager")
# rohan = Employee()

# harry.name = "harry"
# harry.salary = 5000
# harry.role = "Manager"
#
# rohan.name = "rohan"
# rohan.salary = 3500
# rohan.role = "assistant manager"
# rohan.no_of_leaves = 4
print(harry.role)