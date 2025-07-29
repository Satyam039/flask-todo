from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017")
db = client.todo_db

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    data = {
        "itemName": request.form['itemName'],
        "itemDescription": request.form['itemDescription']
    }
    db.todos.insert_one(data)
    return jsonify({"status": "success"}), 201
