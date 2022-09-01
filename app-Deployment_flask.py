# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 18:49:10 2022

@author: eklou
"""

# Import Flask
import numpy as np
from flask import Flask, request, render_template
import pickle




app = Flask(__name__)
print(open('mod.pkl', 'rb'))
model = pickle.load(open('mod.pkl', 'rb'))
model

@app.route('/') #http://www.google.com/
def home():
    return render_template('index.html')

@app.route('/predict', methods =['POST'])
def predict():
    '''
    For rendering result on HTML GUI
    '''
    int_features = [int(x) for x in request.form.value()]
    final_features = [np.array(int_features)]
   # prediction = model.predict(final_features)
    
    #output = round(prediction[0], 2)
    
   # return render_template('index.html', prediction_text='Price Charged should be $ {}' .format(output))

if __name__=="__main__":    

    app.run(port=5000, debug= False)