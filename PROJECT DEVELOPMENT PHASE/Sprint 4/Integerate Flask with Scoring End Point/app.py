import flask
from flask import request, render_template
from flask_cors import CORS
import requests

import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "<L0Tb5y6cXGzzoPYEMXM-XXZTmAgzVQgLJ2HTlRUlkVn9>"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}


app = flask.Flask(__name__, static_url_path='')
CORS(app)
@app.route('/', methods=['GET'])
def sendHomePage():
    return render_template('index1.html')
@app.route('/predict', methods=['POST'])
def predictSpecies():
    a1 = float(request.form['a1'])
    b1 = float(request.form['b1'])
    c1 = float(request.form['c1'])
    d1 = float(request.form['d1'])
    e1 = float(request.form['e1'])
    f1 = float(request.form['f1'])
    g1 = float(request.form['g1'])
    h1 = float(request.form['h1'])
    i1 = float(request.form['i1'])
    j1 = float(request.form['j1'])
    k1 = float(request.form['k1'])
    l1 = float(request.form['l1'])

    X = [[a1, b1, c1, d1, e1, f1, g1, h1, i1, j1, k1, l1]]
   

# NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"input_data": [{"field": [['a1','b1','c1','d1','e1','f1','g1','h1','i1','j1','k1','l1']], "values": X}]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/96c39faa-abfd-47bd-ad20-884c3c9472ef/predictions?version=2022-11-16',json=payload_scoring,header={'Authorization':'Bearer' + mltoken})
 
    print("Scoring response")
    print(response_scoring)
    predictions = response_scoring.json()
    predict = predictions['predictions'][0]['values'][0][0]
    print("Final prediction :",predict)

  # showing the prediction results in a UI# showing the prediction results in a UI
    return render_template('predict.html', predict=predict)

if __name__ == '__main__' :
    app.run(debug= False)