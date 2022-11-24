import flask
from flask import request, render_template
from flask_cors import CORS
import pickle
 
app = flask.Flask(__name__, static_url_path='')
CORS(app)
 
@app.route('/', methods=['GET','POST'])
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
    model = pickle.load(open('CRVP.pkl'))
    species = model.predict(X)
    return render_template('predict.html',predict=species)
 
if __name__ == '__main__':
    app.run()
 


