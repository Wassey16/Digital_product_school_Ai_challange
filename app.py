import json
import pickle

from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)
## Load the model
xg_model=pickle.load(open('xg_model.pkl','rb'))
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict_api',methods=['POST'])
def predict_api():
# Get the data from the request
    data = request.json.get('data')

    if not data:
        return jsonify({"error": "No data provided"}), 400   
     
    year = data['year']
    month = data['month']
    
    input_data = pd.DataFrame({'JAHR': [year], 'MONAT': [month]})

    # Make the prediction
    prediction = xg_model.predict(input_data)[0]
    prediction = float(prediction)
    # Return the prediction as a JSON response
    return jsonify({'prediction': prediction})





if __name__ == "__main__":
    app.run(debug=True)
   
     