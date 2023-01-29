from flask import Flask, render_template, request
import numpy as np
import pickle
import joblib


app = Flask(__name__)

filename = 'file_kahweek3.pkl'

model = joblib.load(filename)

@app.route('/')

def index(): 
    return render_template('index.html')

@app.route('/predict', methods=['POST'])

def predict():
    alcohol = request.form['Alcohol']
    density = request.form['Density']
    volatile_acidity = request.form['Volatile_Acidity']
    chlorides = request.form['Chlorides']
          
    pred = model.predict(np.array([[alcohol, density, volatile_acidity, chlorides]], dtype=float))
    print(pred)
    return render_template('index.html', predict=str(pred))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)