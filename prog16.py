#functions and docstring
#already defined fun
a=6
b=9
sum= sum((a,b))
print(sum)
#user defined fun
def f1():
    print("f1")
f1()

def f2(a,b):
    print(a+b)
f2(5,6)

def average(c,d):
    e=(c+d)/2
    return e
v=average(6,7)
print(v)

#DOCSTRING IN A FUN IS A FIRST LINE DEFINED IN A FUN IN """ """

def average(c,d):
    """this fun doesnt take 3 arguments"""
    e=(c+d)/2
    return e
v=average(6,7)
print(average.__doc__)