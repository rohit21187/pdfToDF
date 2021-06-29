import pandas as pd
import tabula as tab
import numpy as np

df = tab.read_pdf('C:\\Users\\rohit\\Downloads\\ug_email_list_upload.pdf',pages="all",lattice=True)
#for i in range(1,len(df1)):
#    df1[0] = pd.concat([df1[0], df1[i]], ignore_index=True)
df[0].columns=list(df[0].iloc[0])
for i in range(1,len(df)): #cause column in 1st page is the required column

    df1 = pd.DataFrame([df[i].columns.values],columns=list(df[i].columns.values))  #created a df as the column here is a required data
    df[i]= pd.concat([df1,df[i]],ignore_index=True) # concat both df wrote df1 first as it will save us from sorting it agian
    df[i].columns= list(df[0].iloc[0])
    df[0]= pd.concat([df[0],df[i]],ignore_index=True)
df[0].drop(columns=['Password'],inplace=True)
df[0].drop([0],inplace=True)
df[0].reset_index(inplace=True)
df[0].drop(columns=['index'],inplace=True)

new_col= df[0]['Email'].str.split(".", n = 1, expand = True)
need= new_col[1].str.split("@",n=1,expand=True)
df[0]['RegNo']=need[0]
#print(df[0])
#df[0].to_csv('C:\\Users\\rohit\\Downloads\\Email.csv')
