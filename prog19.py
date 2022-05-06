#writing, appending and doing both the things in a file
#write mode
f = open("sharma1","w")
a= f.write("today is a good day indeed")
print(a)
f.close()
# #append mode
f = open("sharma2","a")
b= f.write("today is a good day indeed")
print(a)
f.close
#read+write
f = open("sharma1","r+")
z= f.read()
print(z)
a=f.write("aj mosam bda baiman h")
print(a)


