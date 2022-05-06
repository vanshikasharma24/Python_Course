#open with with
with open("vanshika","r") as f:
    print(f.readline())
    print(f.readlines())
    print(f.readline())

#after readlines readline wont work since it has already read all the lines
#to make it work we have to open the pointer again
f= open("vanshika","r")
print(f.readline())