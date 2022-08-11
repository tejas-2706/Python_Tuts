class Employee:
    no_of_leaves = 10
    pass

harry = Employee()
rohan = Employee()

harry.name = "harry"
harry.salary = 5000
harry.role = "Manager"

rohan.name = "rohan"
rohan.salary = 3500
rohan.role = "assistant manager"
print(Employee.no_of_leaves)
print(rohan.__dict__)
Employee.no_of_leaves = 30
print(Employee.__dict__)
print(Employee.no_of_leaves)