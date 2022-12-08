import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import seaborn as sns

data=pd.read_csv('../cleanedDataWithNames.csv')
noCat=data.drop(columns=['Tm','Pos','Name'])

labels=data['Pos'].unique()
colors = {'SG': 'b', 'PG': 'r', 'SF': 'g', 'PF':'k','C':'y'}
'''
logSalary=np.log(noCat['Salary'])
print(stats.normaltest(logSalary).pvalue)

sqrtSalary=np.sqrt(noCat['Salary'])
print(stats.normaltest(sqrtSalary).pvalue)

sqSalary=noCat['Salary']**2
print(stats.normaltest(sqSalary).pvalue)

boxSalary,bestLambda=stats.boxcox(noCat['Salary'])   
plt.hist(boxSalary) 
plt.show()
'''
C=data[data['Pos']=='C']
SG=data[data['Pos']=='SG']
SF=data[data['Pos']=='SF']
PF=data[data['Pos']=='PF']
PG=data[data['Pos']=='PG']

#C Normality test
C_salary=C['Salary']
plt.hist(C_salary,alpha=0.5,color='y')
plt.ylabel('Count')
plt.xlabel('Salary')
plt.title("Center Histogram")
sns.set()
plt.show()

#SG Normality test
SG_salary=SG['Salary']
plt.hist(SG_salary,alpha=0.5,color='b')
plt.ylabel('Count')
plt.xlabel('Salary')
plt.title("Shooting Guard Histogram")
sns.set()
plt.show()
    
#SF Normality test
SF_salary=SF['Salary']
plt.hist(SF_salary,alpha=0.5,color='g')
plt.ylabel('Count')
plt.xlabel('Salary')
plt.title('Small Forward Histogram')
sns.set()
plt.show()
#PF Normality test
PF_salary=PF['Salary']
plt.hist(PF_salary,alpha=0.5,color='k')
plt.ylabel('Count')
plt.xlabel('Salary')
plt.title('Power Forward Histogram')
sns.set()
plt.show()

#PG Normality  test
PG_salary=PG['Salary']
plt.hist(PG_salary,alpha=0.5,color='r')
plt.ylabel('Count')
plt.xlabel('Salary')
plt.title('Point Guard Histogram')
sns.set()
plt.show()

print("The equal variance test has a p-value of:")
print(stats.levene(PG_salary,PF_salary,SF_salary,SG_salary,C_salary).pvalue)
print("meaning that the position salaries do have equal variance.\n")

boxC_Salary,bestLambdaC=stats.boxcox(C_salary)   
boxSG_Salary,bestLambdaSG=stats.boxcox(SG_salary)   
boxPF_Salary,bestLambdaPF=stats.boxcox(PF_salary)   
boxSF_Salary,bestLambdaSF=stats.boxcox(SF_salary)   
boxPG_Salary,bestLambdaPG=stats.boxcox(PG_salary)   

plt.hist(boxC_Salary,alpha=0.5,color='b')
plt.ylabel('Count')
plt.title('Boxcox Center Salary Histogram')
plt.xlabel('Boxcox Salary')
sns.set()

plt.show()
plt.title('Boxcox Shooting Guard Salary Histogram')
plt.ylabel('Count')
plt.hist(boxSG_Salary,alpha=0.5,color='b')
plt.xlabel('Boxcox Salary')
sns.set()

plt.show()

plt.title('Boxcox Small Forward Salary Histogram')
plt.ylabel('Count')
plt.hist(boxSF_Salary,alpha=0.5,color='b')
plt.xlabel('Boxcox Salary')
sns.set()

plt.show()

plt.ylabel('Count')
plt.xlabel('Boxcox Salary')
plt.title('Boxcox Point Guard Salary Histogram')
plt.hist(boxPG_Salary,alpha=0.5,color='b')
sns.set()
plt.show()

plt.ylabel('Count')
plt.hist(boxPF_Salary,alpha=0.5,color='b')
plt.title('Boxcox Power Forward Salary Histogram')
plt.xlabel('Boxcox Salary')
sns.set()
plt.show()

print("With a box-cox transformation, the equal variance test has a p-value of:")
print(stats.levene(boxPG_Salary,boxPF_Salary,boxSF_Salary,boxSG_Salary,boxC_Salary).pvalue)
print("meaning that position salaries have equal variance.\n")

#
C_salary=C_salary.rename('C_Salary')
SG_salary=SG_salary.rename('SG_Salary')
SF_salary=SF_salary.rename('SF_Salary')
PF_salary=PF_salary.rename('PF_Salary')
PG_salary=PG_salary.rename('PG_Salary')

#Resetting indices to join
C_salary.reset_index(drop=True, inplace=True)
SG_salary.reset_index(drop=True, inplace=True)
SF_salary.reset_index(drop=True, inplace=True)
PF_salary.reset_index(drop=True, inplace=True)
PG_salary.reset_index(drop=True, inplace=True)

#Joining
salaries=pd.concat([C_salary,SG_salary,SF_salary,PF_salary,PG_salary],axis=1)

#Using Kruskal
Kstats,kPvalue=stats.kruskal(C['Salary'],SG['Salary'],SF['Salary'],PF['Salary'],PG['Salary'])
print("With a p-value of")
print(kPvalue)
print("the Kruskal Wallis H-test concludes that the population medians of the posittion salaries are equal.\n")

melt=pd.melt(salaries)
melt.dropna(inplace=True)
posthoc=pairwise_tukeyhsd(melt['value'], melt['variable'],alpha=0.05)

print(posthoc)
fig = posthoc.plot_simultaneous()
print(fig)

