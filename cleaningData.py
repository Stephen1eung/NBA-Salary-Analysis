import requests
from bs4 import BeautifulSoup
import pandas as pd

#Requesting from url
url='https://hoopshype.com/nba2k/'
website=requests.get(url)

#<Response [200]>

#Finding the relevant table
text=BeautifulSoup(website.text,'html')
table=text.find('table',{'class':'hh-salaries-ranking-table hh-salaries-table-sortable responsive'})

#Identifying column name of dataframe
colNames=['Rank','Name','Rating']
ratingData=pd.DataFrame(columns=colNames)

#Extracting relevant rows
for i in table.find_all('tr')[1:]:
 rows=i.find_all('td')
 row = [j.text for j in rows]
 length=len(ratingData)
 ratingData.loc[length]=row

#Getting rid of spaces and tabs 
ratingData['Rank']=ratingData['Rank'].str.extract('(\d+)')
ratingData['Name']=ratingData['Name'].str.extract('([a-zA-Z\" "]+)')
ratingData['Rating']=ratingData['Rating'].str.extract('(\d+)')

#Saving to csv
ratingData.to_csv('NBA2KRating.csv',index=False)
