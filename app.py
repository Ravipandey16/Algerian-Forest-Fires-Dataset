import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
import os
from sklearn.preprocessing import StandardScaler


application = Flask(__name__)
app=application


##import ride regressor and standard scaler pickle
ridge_model=pickle.load(open('models/ridge.pkl','rb'))
standard_scaler=pickle.load(open('models/scaler.pkl','rb'))


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')


@app.route("/predictdata", methods=['GET','POST'])
def predict_datapoint():
    if request.method=='POST':
        temperature = request.form.get('Temperature')
        rh = request.form.get('RH')
        ws = request.form.get('Ws')
        rain = request.form.get('Rain')
        ffmc = request.form.get('FFMC')
        dmc = request.form.get('DMC')
        isi = request.form.get('ISI')
        classes = request.form.get('Classes')
        region = request.form.get('Region')

        new_data_scaled=standard_scaler.transform([[temperature, rh, ws, rain, ffmc, dmc, isi,classes, region]]) 
        result = ridge_model.predict(new_data_scaled)

        return render_template('home.html', results=result[0])   
    else:
        return render_template('home.html')
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
