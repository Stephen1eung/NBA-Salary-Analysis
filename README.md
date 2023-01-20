# NBA Statistics Analysis Using Regression Models

## Introduction
We wanted to analyze the salaries of NBA players, to determine if there exists a difference in the salaries of the players depending on what position they played. We also wanted to analyze to see if NBA players had an increase in wage depending on different features such as their popularity on instagram or their age. There were four main data files used in this project: NBA salaries, NBA 2k ratings, NBA player Instagram followers, and NBA player statistics. The data was scraped off of three NBA data sources: Basketball References, Popular Basketballers, and HoopsHype.   
## Commands
As there were no files that needed to be run through the command line, the files can all be run as simple python files. 

## Required Libraries:
import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt  

from sklearn.linear_model import LinearRegression  
from sklearn.neighbors import KNeighborsRegressor  
from sklearn.ensemble import RandomForestRegressor  
from sklearn.neural_network import MLPRegressor  

from sklearn.preprocessing import MinMaxScaler  
from sklearn.pipeline import make_pipeline  
from sklearn.model_selection import train_test_split  

import re    
from unidecode import unidecode  
import requests  
from bs4 import BeautifulSoup  

import seaborn as sns  
from scipy import stats  


## Order of Execution   
1. Webscraping Directory   
The webscraping directory will be used first to scrape the relevant data files from various websites. As these files are independent, they can be used in any order.    
  
  - salaryWebscraping.py to scrape the salary data from https://hoopshype.com/salaries/players/.  
  - ratingWebscraping.py to scrape the rating data from https://hoopshype.com/nba2k/.    
  - playerStatsScraping.py to scrape player statistics from https://www.basketball-reference.com/leagues/NBA_2023_totals.html.    
  - followingWebscraping.py to scrape player statistics from https://www.popularbasketballers.com/.    
      
2. Cleaning Data     
Once the data has been scraped into the subdirectory Datasets, cleaningData.py will be used to clean it so it can be used for analysis.     
 
3. Plots directory      
The plots directory created multiple plots on the top salaries of the players by position and the overall top salaries.      

4. Hypothesis Testing directory      
   The hypothesis testing directory tested the question "Is there a difference in the salaries of the players depending on what position they play."       
   
5. NBA process  

The NBA-process.py file is where the 4 models: MLP, Linear Regression, Kneighbors, Random Forest were fit to see if we could find the most impactful features used to predcit a NBA player's salary.  

## Files produced/Expected  
plots.py produced 5 plots on the top 5 players salaries depending on their position. It also produced the top 20 salaries of all NBA players.   

hypothesisTesting.py produced 10 plots on the distribution of the player's salaries based off of position. 5 of the plots were the original dataset. The other 5 were after a boxcox transformation.  

NBA-proccess.py produced 4 plots of the prediction of salaries made by the 4 models MLP, Linear Regression, Kneighbors, Random Forest vs the actual salaries of the players.   
