# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 20:06:54 2021

@author: HP
"""

"""To do the operations with Operating System, we have to import osops"""

import os

os.mkdir("myfolder")  #create a folder

os.makedirs("fol1/fol2")

os.rmdir("fol1/fol2")


print(os.path.exists("hello.txt")) #Check file exist or not

print(os.path.isdir("fol1")) #Check folder exist or not

""" In this we can run a code at particular time continiously repeatdly, It observe each files and folder
and files inside folder ,and check which one is last time update and modified, if last update file is older
than my threashold, then we delete those files, if not then escape"""
