from flask import Flask,request
import numpy as np
import pickle
app = Flask(__name__)

@app.route("/checkPassenger",methods=['POST'])
def checkPassenger():
    passenger_details=np.array([request.json['passengerId'],request.json['Pclass'],request.json['gender'],request.json['age'],request.json['sibSp'],request.json['parch'],request.json['fare'],request.json['embarked']])
    
    # print("Passenger Details",passenger_details)
   
    model = pickle.load(open('model.pkl', 'rb'))

    # print(model.predict([passenger_details]))

    return str(model.predict([passenger_details])[0][1])
app.run(port=5000,debug=True)