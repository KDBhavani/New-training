# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 14:58:29 2022

@author: sys
"""
import pandas as pd
df=pd.read_excel(r"C:\Users\sys\Bhavani\Data_Engineering.xlsx",sheet_name="Transactions_Details")
pd.pivot_table(df,values='Transaction_amount',index='Customer_ID',aggfunc='count')
df.groupby('Customer_ID')['Transaction_amount'].count()
df=pd.read_excel(r"C:\Users\sys\Bhavani\Data_Engineering.xlsx")
df
df=pd.read_excel(r"C:\Users\sys\Bhavani\Data_Engineering.xlsx",sheet_name="Financial_Details")
df
