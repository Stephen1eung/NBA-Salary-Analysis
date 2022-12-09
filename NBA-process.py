import numpy as np
import pandas as pd
import warnings
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor

from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split


def lin_regression(X_train, X_valid, y_train, y_valid):
    #Scaling features due to extreme large values
    model = make_pipeline(
        MinMaxScaler(),
        LinearRegression())
    
    model.fit(X_train, y_train)
    y_pred = model.predict(X_train)
    
    #Values of validation and prediction values
    prediction = pd.DataFrame({'Actual': y_train[0:50], 'Predicted': y_pred[0:50]})

    prediction.plot(kind='bar',figsize=(10,6))
    plt.title("Linear Regression")
    plt.xlabel(' ')
    plt.ylabel('Salary')
    plt.ticklabel_format(style='plain',axis='y')
    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    
    #Evaluation of score for overfitting / underfitting
    print("Linear Regression Training Score: " + str(model.score(X_train, y_train)))
    print("Linear Regression Validation Score: " + str(model.score(X_valid, y_valid)) +'\n')
    

def ranforest_regression(X_train, X_valid, y_train, y_valid):    
    model = RandomForestRegressor(n_estimators=100, max_depth=2, min_samples_leaf=3)

    model.fit(X_train, y_train)
    y_pred = model.predict(X_train)
    
    #Values of validation and prediction values
    prediction = pd.DataFrame({'Actual': y_train[0:50], 'Predicted': y_pred[0:50]})
    #Prediction of importance of each feature
    importance = pd.DataFrame({'Feature': list(noSalary), 'Importance': model.feature_importances_})
    
    prediction.plot(kind='bar',figsize=(10,6))
    plt.title("Random Forest Regression")
    plt.xlabel(' ')
    plt.ylabel('Salary')
    plt.ticklabel_format(style='plain',axis='y')
    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    
    #Evaluation of score for overfitting / underfitting
    print("Random Forest Regressor Training Score: " + str(model.score(X_train, y_train)))
    print("Random Forest Regressor Validation Score: " + str(model.score(X_valid, y_valid))+'\n')
    
    print("Random Forest Importance:")
    print(importance)
    
    
def Kneighbor_regression(X_train, X_valid, y_train, y_valid, n):
    model = make_pipeline(
        MinMaxScaler(),
        KNeighborsRegressor(n)) 
    
    model.fit(X_train, y_train)
    y_pred = model.predict(X_train)
    
    #Values of validation and prediction values
    prediction = pd.DataFrame({'Actual': y_train[0:50], 'Predicted': y_pred[0:50]})
    
    prediction.plot(kind='bar',figsize=(10,6))
    plt.title("KNeighbors Regression")
    plt.xlabel(' ')
    plt.ylabel('Salary')
    plt.ticklabel_format(style='plain',axis='y')
    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    
    #Evaluation of score for overfitting / underfitting
    print("KNeighbors Regressor Training Score: " + str(model.score(X_train, y_train)))
    print("KNeighbors Regressor Validation Score: " + str(model.score(X_valid, y_valid))+'\n')
    

def MLP_regression(X_train, X_valid, y_train, y_valid):
    model = make_pipeline(
        MinMaxScaler(),
        MLPRegressor(activation='relu', solver='lbfgs')) 
    
    model.fit(X_train, y_train)
    y_pred = model.predict(X_train)

    #Values of validation and prediction values
    prediction = pd.DataFrame({'Actual': y_train[0:50], 'Predicted': y_pred[0:50]})
    
    prediction.plot(kind='bar',figsize=(10,6))
    plt.title("MLP Regression")
    plt.xlabel(' ')
    plt.ylabel('Salary')
    plt.ticklabel_format(style='plain',axis='y')
    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    
    #Evaluation of score for overfitting / underfitting
    print("MLP Regressor Training Score: " + str(model.score(X_train, y_train)))
    print("MLP Regressor Validation Score: " + str(model.score(X_valid, y_valid))+'\n')


def correlation(dataset, threshold):
    col_corr = set()  
    corr_matrix = dataset.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i, j]) > threshold:
                colname = corr_matrix.columns[i]  
                col_corr.add(colname)
    return col_corr


warnings.filterwarnings('ignore')
data = pd.read_csv('cleanedData.csv')
data = data.drop('Pos',axis=1)
data = data.drop('Tm',axis=1)

noSalary = data.drop(columns=['Salary'])

X = noSalary
y = data['Salary']

X_train, X_valid, y_train, y_valid = train_test_split(X, y, random_state=30)

#correlation data
corr_ft = correlation(X_train, 0.8)
X_train.drop(corr_ft,axis=1,inplace=True)
X_valid.drop(corr_ft,axis=1,inplace=True)
X_traincols=X_train.columns
noSalary.drop(columns=[col for col in noSalary if col not in X_traincols], inplace=True)

lin_regression(X_train, X_valid, y_train, y_valid)
Kneighbor_regression(X_train, X_valid, y_train, y_valid, 6)
MLP_regression(X_train, X_valid, y_train, y_valid)
ranforest_regression(X_train, X_valid, y_train, y_valid)
