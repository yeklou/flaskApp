# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 18:49:10 2022

@author: eklou
"""

# Imort Flask
import pickle
from flask import Flask

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))
#model

@app.route('/') #http://www.google.com/
def home():
    return "Hello, world!"

app.run(port=5000)