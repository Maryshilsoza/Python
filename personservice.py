import json
from persondao import persondao

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/person",methods=["GET"])
def getPerson():
    return "all users"

@app.route("/person",methods=["POST"])
def createPerson():
    record = json.loads(request.data) 
    pd=persondao()
    pd.insertPerson(record)
    return "user created"

@app.route("/person",methods=["PUT"])
def updatePerson():
    return "user update"

@app.route("/person",methods=["DELETE"])
def deletePerson():
    return "user delete"


app.run(port=5000)