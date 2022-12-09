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
    prediction = pd.DataFrame({'Actual': y_train, 'Predicted': y_pred})
    
    #plotting
    prediction.plot(kind='bar',figsize=(10,6))
    plt.title("Linear Regression")
    plt.xlabel(' ')
    plt.ylabel('Salary')
    plt.ticklabel_format(style='plain',axis='y')
    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    
    #Evaluation of score for overfitting / underfitting
    print("Linear Regression Training Score:" + str(model.score(X_train, y_train)))
    print("Linear Regression Validation Score:" + str(model.score(X_valid, y_valid)) +'\n')
    

def ranforest_regression(X_train, X_valid, y_train, y_valid):
    model = RandomForestRegressor(n_estimators=100, max_depth=3, min_samples_leaf=3)
    
    model.fit(X_train, y_train)
    y_pred = model.predict(X_train)
    
    #Values of validation and prediction values
    prediction = pd.DataFrame({'Actual': y_train, 'Predicted': y_pred})
    #Prediction of importance of each feature
    importance = pd.DataFrame({'Feature': list(noSalary), 'Importance': model.feature_importances_})
    #print("Random Forest Importance:")
    #print(importance)
    
    #plotting
    prediction.plot(kind='bar',figsize=(10,6))
    plt.title("Random Forest Regression")
    plt.xlabel(' ')
    plt.ylabel('Salary')
    plt.ticklabel_format(style='plain',axis='y')
    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    
    #Evaluation of score for overfitting / underfitting
    print("Random Forest Regressor Training Score:" + str(model.score(X_train, y_train)))
    print("Random Forest Regressor Validation Score:" + str(model.score(X_valid, y_valid))+'\n')
    
    
def Kneighbor_regression(X_train, X_valid, y_train, y_valid, n):
    model = make_pipeline(
        MinMaxScaler(),
        KNeighborsRegressor(5)) 
    
    model.fit(X_train, y_train)
    y_pred = model.predict(X_train)
    
    #Values of validation and prediction values
    prediction = pd.DataFrame({'Actual': y_train, 'Predicted': y_pred})
    
    #plotting
    prediction.plot(kind='bar',figsize=(10,6))
    plt.title("KNeighbors Regression")
    plt.xlabel(' ')
    plt.ylabel('Salary')
    plt.ticklabel_format(style='plain',axis='y')
    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    
    #Evaluation of score for overfitting / underfitting
    print("KNeighbors Regressor Training Score:" + str(model.score(X_train, y_train)))
    print("KNeighbors Regressor Validation Score:" + str(model.score(X_valid, y_valid))+'\n')
    

def MLP_regression(X_train, X_valid, y_train, y_valid):
    model = make_pipeline(
        MinMaxScaler(),
        MLPRegressor(activation='relu', solver='lbfgs')) 
    
    model.fit(X_train, y_train)
    y_pred = model.predict(X_train)

    #Values of validation and prediction values
    prediction = pd.DataFrame({'Actual': y_train, 'Predicted': y_pred})
    
    #plotting
    prediction.plot(kind='bar',figsize=(10,6))
    plt.title("MLP Regression")
    plt.xlabel(' ')
    plt.ylabel('Salary')
    plt.ticklabel_format(style='plain',axis='y')
    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    
    #Evaluation of score for overfitting / underfitting
    print("MLP Regressor Training Score:" + str(model.score(X_train, y_train)))
    print("MLP Regressor Validation Score:" + str(model.score(X_valid, y_valid))+'\n')


warnings.filterwarnings('ignore')
data = pd.read_csv('cleanedData.csv')
data = data.drop('Pos',axis=1)
data = data.drop('Tm',axis=1)
data = data.head(75)

noSalary = data.drop(columns=['Salary'])

X = noSalary
y = data['Salary']

X_train, X_valid, y_train, y_valid = train_test_split(X, y)

lin_regression(X_train, X_valid, y_train, y_valid)
ranforest_regression(X_train, X_valid, y_train, y_valid)
Kneighbor_regression(X_train, X_valid, y_train, y_valid, 5)
MLP_regression(X_train, X_valid, y_train, y_valid)
    

