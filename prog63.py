#library management system
class Library:
    def __init__(self,listofbooks,libraryname):
        self.listofbooks=listofbooks
        self.libraryname=libraryname
    def displaybooks(self):
        return f"the total books in the library are as follows:{self.listofbooks}"
    # def lendbook(self):

a=int(input("enter number of books to be displayed"))
libraryname=input("type your library name ")
i=0
listofbooks=[]
while(i<a):
    lstinput=input("write your book")
    listofbooks=listofbooks.append(lstinput)
    i=i+1


