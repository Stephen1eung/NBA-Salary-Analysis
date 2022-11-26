import requests
from bs4 import BeautifulSoup
import pandas as pd

#Requesting from url
url='https://www.popularbasketballers.com/'
website=requests.get(url)
#<Response [200]>

#Finding the relevant table
text=BeautifulSoup(website.text,'lxml')
table=text.find('table',id='myTable')

#Identifying column names of dataframe
colNames=[]
for name in table.find_all('th'):
 colName = name.text
 colNames.append(colName)
 
followerData=pd.DataFrame(columns=colNames)

#Extracting relevant rows 
for i in table.find_all('tr')[1:]:
 rows=i.find_all('td')
 row = [j.text for j in rows]
 length=len(followerData)
 followerData.loc[length] = row

#Saving to csv
followerData.to_csv('InstagramFollowers.csv',index=False)