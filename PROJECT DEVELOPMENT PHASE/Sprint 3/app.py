import flask
from flask import request, render_template
from flask_cors import CORS
import joblib
 
app = flask.Flask(__name__, static_url_path='')
CORS(app)
 
@app.route('/', methods=['GET'])
def sendHomePage():
    return render_template('index1.html')
 
@app.route('/predict', methods=['POST'])
def predictSpecies():
    A=float(request.form['A'])
    B=float(request.form['B'])
    C=float(request.form['C'])
    D=float(request.form['D'])
    E=float(request.form['E'])
    F=float(request.form['F'])
    G=float(request.form['G'])
    H=float(request.form['H'])
    I=float(request.form['I'])
    J=float(request.form['J'])
    K=float(request.form['K'])
    L=float(request.form['L'])
    X=[[A,B,C,D,E,
    F,G,H,I,J,K,L]]
    model = joblib.load('CRF.pkl')
    species = model.predict(X)[0]
    return render_template('predict.html',predict=species)
 
if __name__ == '__main__':
    app.run(debug= True)
 


