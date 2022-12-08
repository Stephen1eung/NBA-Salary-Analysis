import pandas as pd
import numpy as np

#Reading in the relevant files
following=pd.read_csv('InstagramFollowers.csv')
playerStats=pd.read_csv('playerStats.csv')
salary=pd.read_csv('NBA2022Salary.csv')
rating=pd.read_csv('NBA2kRating.csv')

#Dropping and renaming features
salary.drop(columns=['number'],inplace=True)
salary.rename(columns={'2022':'Salary'}, inplace=True)
following.drop(columns=['Rank'],inplace=True)
rating.drop(columns=['Rank'],inplace=True)

#Merging data files
data=pd.merge(playerStats,salary,on="Player",how="inner")
data1=pd.merge(rating,following,on="Name",how="inner")
data.rename(columns={'Player':'Name'}, inplace=True)
data=pd.merge(data,data1,on="Name",how="inner")

#Removing players with missing data
data.dropna(inplace=True)

#Sorting by salary and removing player names
data=data.sort_values(by=["Salary"],ascending=False)
data['Instagram Followers'].replace(',','', regex=True, inplace=True)
data['Instagram Followers']=pd.to_numeric(data['Instagram Followers'])
print(data.dtypes)

data.to_csv('cleanedDataWithNames.csv',index=False)
data.drop(columns=["Name"],inplace=True)

data.to_csv('cleanedData.csv',index=False)