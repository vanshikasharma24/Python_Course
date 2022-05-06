#object introspection
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

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
emp1=Employee("hii","hey")
print(type(emp1))
print(type("this is a string"))
print(id("this is a string"))
print(dir("this is a string"))
# dir returns us a list of attributes and methods associated with an object.
print(dir(emp1))
print(id(emp1))
import inspect
print(inspect.getmembers(emp1))