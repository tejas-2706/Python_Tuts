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

ram_supporter = Employee("ram", "supporter")
# shaam_fan = Employee("shaam","fan")
print(ram_supporter.email)
ram_supporter.fname = "india"
print(ram_supporter.email)
ram_supporter = "changer.free@legend.com"
print(ram_supporter.fname)

del ram_supporter.email
print(ram_supporter.email)
ram_supporter.email = "Harry.Perry@codewithharry.com"
print(ram_supporter.email)

