# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 20:55:26 2019

@author: home
"""

import pandas as pd
class pred:
    def prediction(n):
        print(n)
        df = pd.read_csv('prediction.csv')
        for i in df.fname:
            if(i==n):
                a=i
        c=df[df.fname==a]
        df1= pd.DataFrame(c)
        df1.reset_index(drop=True, inplace=True)
        return (df1[df1['y_pred']]*100)
    
    
    
    
    
    