# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 22:30:33 2022

@author: eklou
"""

#Import packages
import pickle
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

#Import data
df_Cab = pd.read_csv("Cab_Data.csv")

class Price_Charged
#Visualize the data
df_Cab.head()


X= df_Cab[['KM Travelled', 'Cost of Trip']]
Y= df_Cab['Price Charged'] 

#Create a model and fit it
model = LinearRegression().fit(X, Y)


#Get results
r_sq = model.score(X, Y)

print(f"coefficient of determination: {r_sq}")

print(f"intercept: {model.intercept_}")

print(f"slope: {model.coef_}")

#Predict Response

y_pred = model.predict(X)
pred_df = pd.DataFrame({'KM Travelled': df_Cab['KM Travelled'],'Cost of Trip': df_Cab['Cost of Trip'], 
                        'Actual Price Charged': Y, 'Predicted Price Charged': y_pred,})
print(f"predicted response:\n{y_pred}")
print(f"Price Charged:\n{pred_df}")

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
    print("Pickling complete")
