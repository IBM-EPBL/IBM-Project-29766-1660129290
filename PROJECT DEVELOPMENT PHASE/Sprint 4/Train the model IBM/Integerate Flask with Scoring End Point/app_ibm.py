import requests

import flask
from flask import request, render_template
from flask_cors import CORS
import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "L2-2mOdnEHfsfjmxoRUJcEfaafQ7LUIQgC0vCzJX4mRH"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}


app = flask.Flask(__name__, static_url_path='')
CORS(app)
@app.route('/', methods=['GET'])
def sendHomePage():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predictSpecies():
    A1 = float(request.form['Al'])
    B1 = float(request.form['B1'])
    C1 = float(request.form['C1'])
    D1 = float(request.form['D1'])
    E1 = float(request.form['E1'])
    F1 = float(request.form['F1'])
    G1 = float(request.form['G1'])
    H1 = float(request.form['H1'])
    I1 = float(request.form['I1'])
    J1 = float(request.form['J1'])
    K1 = float(request.form['K1'])
    L1 = float(request.form['L1'])

    X = [[A1,B1,C1,D1,E1,F1,G1,H1,I1,J1,K1,L1]]
   
    payload_scoring = {"input_data": [{"field": [['Al','B1','C1','D1','E1','F1','G','H','I','J','K','L']], "values": X}]}
    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/d4e91d52-c725-4b14-ba56-891a6aa19ba0/predictions?version=2022-11-18', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
    print(response_scoring)
    predictions = response_scoring.json()
    predict = predictions['predictions']
    print("Final prediction :",predict)
    
    # showing the prediction results in a UI# showing the prediction results in a UI
    return render_template('predict.html', predict=predict)

if __name__ == '__main__' :
    app.run(debug= False)

