from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import ms
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression
import pandas as pd

#Treinamento do modelo de Regressão Linear
def train_model_regressao(x,y):
    x_train, x_test, y_train, y_test = ms(x,y,test_size=0.2, random_state=100)
    model = LinearRegression()
    model.fit(x_train, y_train)
    return model, x_test , y_test
#Treinamento do modelo de RandomForest
def train_model_forest(X,Y):
    X_train, X_test, Y_train, Y_test = ms(X,Y, test_size=0.2,random_state=100)
    rf = RandomForestRegressor(max_depth=2,random_state=100)
    rf.fit(X_train, Y_train)

