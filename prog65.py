#Pickle comes in handy while saving complicated data.
#The pickled file generated is not easily readable and thus provides some level of security
# import pickle
# car=["x","y","z"]
# file="mycar.pkl"
# fileobj=open(file,"wb")
# pickle.dump(car,fileobj)

#to retrieve file
import pickle

file="mycar.pkl"
fileobj=open(file,"rb")

mycar=pickle.load(fileobj)
print(mycar)
print(type(mycar))
