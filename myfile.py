# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 19:36:41 2021

@author: HP
"""

""" This Project relate to Delete the Old files "Auto delete Old Files" As we have so many task to read,
write and delete files from server, Suppose we have a collection of lots of movie, and want to delete 
the oldest ones """


myfile = open("hello.txt","wt") #writing in file

print("I am so Happy", file=myfile) 

myfile.close()
