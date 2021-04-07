# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 19:40:22 2020

@author: dbda
"""

import pandas as pd
df=pd.read_csv(r"F:\Zomato\zomato_new_file.csv")

cuisines_combo=df['cuisines']

cuisine_names =set()
for s in cuisines_combo:
    for i in s.split(","):
        cuisine_names.add(i.strip(" "))

cuisines =[]
for s in cuisines_combo:
    l=[]
    for i in s.split(","):
        l.append(i.strip(" "))
    cuisines.append(l)
        
len(cuisine_names)
    
######### new df for cuisines
from mlxtend.preprocessing import TransactionEncoder

te = TransactionEncoder()
te_ary = te.fit(cuisines).transform(cuisines)
te_ary_int = te_ary.astype(int)

te_ary_int.shape

df_cuisines = pd.DataFrame(data = te_ary_int,index = df.index, columns = list(cuisine_names))

##### Merge two dfs

final_df = df.merge(df_cuisines,left_index = True,right_index = True)
df.shape
df_cuisines.shape
final_df.shape


###############for highlights
highlights_combo=df['highlights']

highlights_names =set()
for j in highlights_combo:
    for i in j.split(","):
        n = i.strip(" ").strip("]").strip("[").strip("'")
        highlights_names.add(n)
        
len(highlights_names)

highlights =[]
for j in highlights_combo:
    h=[]
    for i in j.split(","):
        n = i.strip(" ").strip("]").strip("[").strip("'")
        h.append(n)
    highlights.append(h)
        
len(highlights)
   
######### new df for cuisines
from mlxtend.preprocessing import TransactionEncoder

te2 = TransactionEncoder()
te2_ary = te2.fit(highlights).transform(highlights)
te2_ary_int = te2_ary.astype(int)

te2_ary_int.shape

df_highlights = pd.DataFrame(data = te2_ary_int,index = df.index, columns = list(highlights_names))

##### Merge two dfs

final_df1 = final_df.merge(df_highlights,left_index = True,right_index = True)
final_df
df_highlights.shape
final_df1.shape

final_df1.to_csv("F:\\Zomato\\large_zomato_211.csv")



