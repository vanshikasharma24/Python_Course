#more on files
f= open("vanshika","r")

#tell function
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())
#seek function
print(f.readline())
print(f.readline())
f.seek(5)
print(f.readline())
f.close()