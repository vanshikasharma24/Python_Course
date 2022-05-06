#static method
#unlike, class method, a static method cannot alter or change any variable value or state of the class.
#They are only formed in a class so that only the class instances can access them.
#methods and constructor
class Employee:
    no_of_leaves=7#class variable
    #"Constructor in Python is used to assign values to the variables or data members of a class when an object is created."

    def __init__(self,astd,asalary,arole):
        self.std=astd
        self.salary=asalary
        self.role=arole
    def printdetails(self):#object
        print(f"the std is {self.std} salary is {self.salary}and the role is {self.role}")
    @classmethod
    def changed_leaves(cls,new_leaves):
        cls.no_of_leaves=new_leaves
    @staticmethod
    def sum(a,b):
        print("the sum of numbers is",a+b)


#class variable cant be changed by object it can be changed by class only
#class variable is shared by all the instances

harry=Employee(9,455,"instructor")
rohan=Employee(9,4555,"student")
harry.printdetails()
rohan.printdetails()
rohan.changed_leaves(34)
print(rohan.no_of_leaves)
harry.sum(4,5)
Employee.sum(7,9)

#here we cant the change the class var using a instance but we cant do that by a class mathed which will be accesible
# by the instance