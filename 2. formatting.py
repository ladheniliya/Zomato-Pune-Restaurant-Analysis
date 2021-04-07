# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 17:36:43 2020

@author: dbda
"""
import json
 
#iterating folders and files inside it
import os,sys
folder = 'F:/zomato-master/json-data'

for subfolder in os.listdir(folder):
    infoldername = os.path.join(folder,subfolder)
    infoldername = infoldername.replace("\\","/")
    print("infoldername"+infoldername)
    for filename in os.listdir(infoldername):
        print("filename"+filename)
        infilename = os.path.join(infoldername,filename)
        print("infilename"+infilename)
        if not os.path.isfile(infilename): 
            print("does not exist")
            continue
        #replacing }{ with },{
        data_file= open(infilename,'rt',encoding="utf8")
        data = data_file.read()
        data = data.replace('}{','},{')
        data_file.close()
        # writing to file
        data_file= open(infilename, 'wt',encoding="utf8")
        data_file.write('['+data+']')
        data_file.close()

