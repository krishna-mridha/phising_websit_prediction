# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

phish_model = open('phishing.pkl','rb')
model = joblib.load(phish_model)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/',methods=['GET','POST'])
def predict(first_name=None):
    global df
    #first_name = ""
    # input_features = [int(x) for x in request.form.values()]
    # features_value = np.array(input_features)
    if request.method == "POST":
    #     # getting input with name = fname in HTML form
         first_name = request.form.get("fname")
    #     # getting input with name = lname in HTML form
    #      return "Your name is"+first_name
    # # return render_template('index1.html',prediction_text="The name is {}".format(first_name))

         y_Predict = model.predict([first_name])
         if y_Predict == 'bad':
            result = "This is a Phishing Site. Please avoaid this URL"
         else:
            result = "This is not a Phishing Site. You may render this URL"
    return render_template('index.html',prediction_text=result)


if __name__ == "__main__":
    app.run()
