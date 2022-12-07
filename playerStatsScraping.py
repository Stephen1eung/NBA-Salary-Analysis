import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

pattern=re.compile('^\d+$')
pattern2=re.compile('Rk')

#Requesting from url
url='https://www.basketball-reference.com/leagues/NBA_2023_totals.html'
website=requests.get(url)
#<Response [200]>

#Finding the relevant table
text=BeautifulSoup(website.text,'lxml')
table=text.find('table',id='totals_stats')

#Identifying column names of dataframe
colNames=[]

for name in table.find_all('th'): 
 colName = name.text
 m=re.match(pattern,colName)
 if not m:
     m1=re.match(pattern2,colName)
     if not m1:
         if len(colNames) <29:
             colNames.append(colName)
 
playerStats=pd.DataFrame(columns=colNames)

for i in table.find_all('tr')[1:]:
 rows=i.find_all('td')
 row = [j.text for j in rows]
 if row:
     length=len(playerStats)
     playerStats.loc[length]=row

playerStats.to_csv('playerStats.csv',index=False)
