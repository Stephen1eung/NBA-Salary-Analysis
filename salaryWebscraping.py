import requests
from bs4 import BeautifulSoup
import pandas as pd
from unidecode import unidecode
#Requesting from url
url='https://hoopshype.com/salaries/players/'
website=requests.get(url)

#<Response [200]
#Finding the relevant table
text=BeautifulSoup(website.text,'lxml')
table=text.find('table',{'class':'hh-salaries-ranking-table hh-salaries-table-sortable responsive'})

#Identifying column name of dataframe
colNames=['number','Player','2022','2023','2024','2025','2026','2027']
salaryData=pd.DataFrame(columns=colNames)

#Extracting relevant rows
for i in table.find_all('tr')[1:]:
 rows=i.find_all('td')
 row = [j.text for j in rows]
 length=len(salaryData)
 salaryData.loc[length]=row

#Getting rid of spaces and tabs 
salaryData.drop(['2023','2024','2025','2026','2027'],inplace=True,axis=1)
salaryData['number']=salaryData['number'].str.extract('(\d+)')
salaryData['Player']=salaryData['Player'].str.extract('([a-zA-Z\'\-\" "\.\,]+)')
salaryData['Player']=salaryData['Player'].apply(unidecode)
salaryData['2022'].replace(',','', regex=True, inplace=True)
salaryData['2022']=salaryData['2022'].str.extract('(\d+)')
salaryData['Player'].replace('(Jr)$','',regex=True,inplace=True)


#Saving to csv
salaryData.to_csv('NBA2022Salary.csv',index=False)