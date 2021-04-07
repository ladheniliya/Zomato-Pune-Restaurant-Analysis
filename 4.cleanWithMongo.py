# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 17:15:54 2020

@author: dbda
"""
import pymongo 

mongo_client = pymongo.MongoClient('localhost',27017)
database = mongo_client['test_zomato']

# main_zomato is cleaned data
# test_collection is raw data
db1 = database['test_collection']
db = database['fresh_zomato']

db.drop()

result = db1.find({},{'name':1,'location':1,'id':1,'cuisines':1,'timings':1,'average_cost_for_two':1,'price_range':1,'highlights':1,'user_rating':1,'has_online_delivery':1,'has_table_booking':1,'establishment_types':1})

db.insert(result)

db.update_many({},{'$unset':{"user_rating.rating_obj":1,"location.zipcode":1,"location.city":1,"location.city_id":1,"location.country_id":1}})

#db = database['zom']

result = db.find()
#result = db.find({'id': '19296685'})
for record in result:
    # print(record)
    # print("\n")
    record_id = record['_id']
    ## sort cuisines 
    cus = record['cuisines']
    l1=[i.strip(' ') for i in cus.split(",")]
    l1.sort()
    cuisines = ','.join(l1)
    # set locality
    loc = record['location']['locality_verbose']
    add = record['location']['address']
    # print(loc)
    # print(add)
    l2=[i.strip(' ') for i in loc.split(",")]
    if l2[-1].lower() == 'pune':
        if len(l2[-2]) > 20:
            l3=[i.strip(' ') for i in add.split(",")]
            # print(l3)
            if l3[-1].lower() == 'pune':
                db.update_one({'_id':record_id},{'$set':{"location.locality":l3[-2],"cuisines":cuisines}})
        else:
            db.update_one({'_id':record_id},{'$set':{"location.locality":l2[-2],"cuisines":cuisines}})
    else:
        db.update_one({'_id':record_id},{'$set':{"location.locality":l2[-1],"cuisines":cuisines}})

print("Cleaning Done")
    
    # print("Location: ",record['location'])
    # print("Cuisine: ",record['cuisines'])
    # print("\n\n")

# new_result = db.find({'_id':'19110081'})
# print([record for record in new_result])


#'Fast Food, Beverages, Street Food'

# import json

# result = db.find({})
# filename = "F:\\Zomato\\fresh_zomato.json"
# file = open(filename, "w",encoding='utf8')
# #file.write('[')
# for document in result:
#     file.write(json.dumps(document))
#     file.write(',')
# #file.write(']')  

# print("Saved in "+filename)   
