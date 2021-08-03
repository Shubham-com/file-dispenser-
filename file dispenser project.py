# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 20:27:58 2021

@author: HP
"""

import os

from datetime import datetime, timedelta

path = "fol1"

#base is the main file from which we are observing others files that cannot be deleted, here base is fol1
#getmtime is get modification time
#getctime = creation time 

#datetime.now() - timedelta(minutes=1)).timestamp() this time is older 1 min from now in milisec

# if threshold < modified means it is new file and vice versa

#os.listdir(path) provides the internal files or folder

def file_dispenser(path, threshold, base=True):
    
    if os.path.isdir(path):
        for internal in os.listdir(path):
            file_dispenser(path + "/" + internal,threshold, False)
     #   return
        #if inside the folder no files are there
        
        if (not base) and (len(os.listdir(path)) == 0):
            os.rmdir(path)
            
        return
    
    modified = os.path.getmtime(path)
    
    if threshold > modified:
        print("this is an old file")
        os.remove(path)
    else:
        print("this is a new file")
    
threshold = (datetime.now() - timedelta(minutes=1)).timestamp()

#print(threshold)
file_dispenser("fol1",threshold)
    