# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 12:03:32 2020

@author: dell
"""

import numpy as np
import pandas as pd

zom = pd.read_csv(r"F:/zomato-master/zomzom.csv")

x = zom['cuisines'].apply(lambda x: [i.lstrip() for i in x.split(",")])

y = x.tolist()

from mlxtend.preprocessing import TransactionEncoder
te = TransactionEncoder()
te_ary = te.fit(y).transform(y)
te_ary

te_ary.astype("int")

te.columns_

cui = pd.DataFrame(te_ary.astype('int'), columns=te.columns_)

x1 = zom['highlights'].str.replace("'","")
type(x1[0])
x1 = x1.str.replace("[","").str.replace("]","")
x1 = x1.apply(lambda x: [i.lstrip() for i in x.split(",")])

y1 = x1.tolist()

te = TransactionEncoder()
te_ary = te.fit(x1).transform(x1)
te_ary

te_ary.astype("int")

te.columns_

high = pd.DataFrame(te_ary.astype('int'), columns=te.columns_)

final_df = pd.concat([zom,cui,high],axis=1,join="inner")
