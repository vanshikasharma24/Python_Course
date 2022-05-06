#generator
#Iterables are objects that can be placed inside a loop and can return one variable at a time.
#An iterator can be defined as an object that does iterations on iterable.
#Every iterable, either it is a string or tuple, has a built-in method __iter__() that creates an object when called.
#The object moves from character to character of iterable using the __next__() method.
"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration -

"""
def gen(n):
    for i in range(n):
        yield i
g=gen(2)
print(g.__next__())
print(g.__next__())
# print(g.__next__())
v="vanshika"
ier=iter(v)
print(ier.__next__())
#num is not iterable
n=67
ier=iter(6)
print(ier.__next__())
