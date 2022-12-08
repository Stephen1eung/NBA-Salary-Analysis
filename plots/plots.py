import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data=pd.read_csv('../cleanedDataWithNames.csv')
print(data)
noCat=data.drop(columns=['Tm','Pos','Name'])

labels=data['Pos'].unique()
colors = {'SG': 'b', 'PG': 'r', 'SF': 'g', 'PF':'k','C':'y'}
#Top 10 Salary 
plt.subplot(3, 2, 1)
top10Salary=data.head(20)
top10Salary=top10Salary.sort_values(by=['Salary'],ascending=True)
plt.barh(top10Salary['Name'],top10Salary['Salary'], color=[colors[i] for i in top10Salary['Pos']])
plt.ticklabel_format(style='plain',axis='x')
plt.xlabel("Salary")
handles = [plt.Rectangle((0,0),1,1, color=colors[l]) for l in labels]
plt.legend(handles, labels, title="Position")
plt.title('Top 20 Salaries of NBA Players 2022-2023')
    
#Top 5 Salary by position
C=data[data['Pos']=='C']
SG=data[data['Pos']=='SG']
SF=data[data['Pos']=='SF']
PF=data[data['Pos']=='PF']
PG=data[data['Pos']=='PG']

top5Center=C.head(10)
top5Center=top5Center.sort_values(by=['Salary'],ascending=True)
plt.subplot(3, 2, 2)

plt.barh(top5Center['Name'],top5Center['Salary'],color='y')
plt.title('Top 10 Center Salaries 2022-2023')
plt.xlabel("Salary")

top5PG=PG.head(10)
top5PG=top5PG.sort_values(by=['Salary'],ascending=True)
plt.subplot(3, 2, 3)

plt.barh(top5PG['Name'],top5PG['Salary'],color='r')
plt.title('Top 10 Point Guard Salaries 2022-2023')
plt.xlabel("Salary")


top5SG=SG.head(10)
top5SG=top5SG.sort_values(by=['Salary'],ascending=True)
plt.subplot(3, 2, 4)

plt.barh(top5SG['Name'],top5SG['Salary'],color='b')
plt.title('Top 10 Shooting Guard Players Salaries 2022-2023')
plt.xlabel("Salary")

top5PF=PF.head(10)
top5PF=top5PF.sort_values(by=['Salary'],ascending=True)
plt.subplot(3, 2, 5)

plt.barh(top5PF['Name'],top5PF['Salary'],color='k')
plt.title('Top 10 Power Forward Salaries 2022-2023')
plt.xlabel("Salary")

top5SF=SF.head(10)
top5SF=top5SF.sort_values(by=['Salary'],ascending=True)
plt.subplot(3, 2, 6)

plt.barh(top5SF['Name'],top5SF['Salary'],color='g')
plt.title('Top 10 Small Forward Salaries 2022-2023')
plt.xlabel("Salary")
plt.show()