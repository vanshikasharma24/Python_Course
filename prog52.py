#setter and property decorator
# Python property decorator is composed of four things, i.e., getter, setter, deleted, and Doc.
# The first three are methods, and the fourth one is a docstring or comment.
#Use @property along with the getter method to access the value of the attribute.
#@function_name.setter is a setter method with which we can set the value of the attribute
#Setters are a great way of performing encapsulation
#@function_name.deleter is a deleter method which can delete the assigned value by the setter method
class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email="vanshika.sharma@gmail.com"
    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@gmail.com"
    @email.setter
    def email(self,string):
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

vanshika_sharma=Employee("vanshika","sharma")
print(vanshika_sharma.email)
vanshika_sharma.fname="bulbul"
# print(vanshika_sharma.email)
vanshika_sharma.email="bul.sharma@gmail.com"
print(vanshika_sharma.email)
print(vanshika_sharma.fname)
del vanshika_sharma.email
print(vanshika_sharma.email)
#fname in email didnt changed