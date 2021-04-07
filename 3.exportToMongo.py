import json
import pymongo 
mng_client = pymongo.MongoClient('localhost', 27017)
mng_db = mng_client['my_zom'] # Replace mongo db name
collection_name = 'test_collection' # Replace mongo db collection name
db_cm = mng_db['test_collection']
 
#iterating folders and files inside it
import os,sys
folder = 'F:/zomato-master/json-data'

#importing files to mongodb as collections
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
        data_file= open(infilename, 'rt',encoding="utf8")
        data_json = json.loads(data_file.read())
        #Insert Data
        for dict_json in data_json:
            if dict_json['restaurants']!=[]:
                rest_list = dict_json['restaurants']
                for res in rest_list:
                    res['restaurant']['_id'] = res['restaurant']['id']
                    try:
                        db_cm.insert(res['restaurant'])
                    except pymongo.errors.DuplicateKeyError:
                        continue
                
        data_file.close()
        
    
    
    
############################################################################################################
#importing files to mongodb as collections
#data_file= open(r"F:\zomato-master\json-data\Akurdi\Akurdi_7.json", 'rt',encoding="utf8")
#data_json = json.loads(data_file.read())
#type(data_json)
##Insert Data
#
#                
#for dict_json in data_json:
#    if dict_json['restaurants']!=[]:
#        rest_list = dict_json['restaurants']
#        for res in rest_list:
#            res['restaurant']['_id'] = res['restaurant']['id']
#            print(res['restaurant']['_id'])
#
# 
## Query data
#db_cm.UNS_Collection2.find().pretty()
