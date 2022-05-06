#lambda or anonymous fun///one liners
def funname(a,b):
    print(a+b)
funname(9,10)

funname=lambda x,y:x+y;
print(funname(10,9))

# def afirst(a):
#     return a[1]

a= [[1,8],[8,4],[4,6]]
a.sort(key=lambda x:x[1])
print(a)
