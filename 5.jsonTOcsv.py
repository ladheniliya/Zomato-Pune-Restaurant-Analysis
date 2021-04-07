
import pandas as pd
import json

import csv 


################# code to covert json to csv ##################################
f1=open(r"F:\zomato-master\zomzom.json","r",encoding="utf8")
zomato_data = json.loads(f1.read())
f1.close()
type(zomato_data)
len(zomato_data)

df = pd.DataFrame(columns = ['_id', 'name', 'locality','latitude','longitude', 'cuisines', 'timings', 'average_cost_for_two', 'price_range', 'highlights', 'aggregate_rating','votes','rating_text', 'has_online_delivery', 'has_table_booking', 'establishment_name'])


for ind in range(len(zomato_data)):
    dict0 = zomato_data[ind]
    res_id = dict0['_id']
    name = dict0['name']
    locality = dict0['location']["locality"]
    longitude=dict0['location']["longitude"]
    latitude=dict0['location']["latitude"]
    cuisines = dict0['cuisines']
    timings = dict0['timings'].replace(' – ','to')
    avg_cost = dict0['average_cost_for_two']
    price_range = dict0['price_range']
    highlights = dict0['highlights']
    aggregate_rating = dict0['user_rating']['aggregate_rating']
    votes = dict0['user_rating']['votes'] 
    rating_text = dict0['user_rating']['rating_text']
    # user = [i['photo']['user'] for i in dict0['restaurant']['photos']] if 'photos' in dict0['restaurant'] else ["null"]
    has_online_delivery = dict0['has_online_delivery']
    has_table_booking = dict0['has_table_booking']
    establishment_name= dict0['establishment_types']['establishment_type']['name'].replace('Café','Cafe')   
    
    df.loc[ind] = [res_id] + [name] + [locality] + [latitude] + [longitude] + [cuisines] + [timings] + [avg_cost] + [price_range] + [highlights] + [aggregate_rating]+ [votes] + [rating_text] + [has_online_delivery] + [has_table_booking] + [establishment_name]
   


df.to_csv('F:\zomato-master\zomzom.csv')

#df['cuisines'].head(10)
#
#
#df['cuisines'] = df['cuisines'].str.replace(',' , '') 
#df['cuisines'] = df['cuisines'].astype(str).apply(lambda x: ' '.join(sorted(x.split())))
#df['cuisines'].value_counts().head()
#
#
