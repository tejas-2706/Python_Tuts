class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@legend.com"
    def explain(self):
        return f"This Employee is {self.fname} {self.lname}"
    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "email is not set"
        return f"{self.fname}.{self.lname}@legend.com"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

skillf = Employee("skill","F")
# print(skillf.email)

print(type("this is sa string"))
print(id("this is sa string"))

o = "this is a string"
print(dir(o))

print(dir(skillf))

