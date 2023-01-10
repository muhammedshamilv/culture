from flask import jsonify
def home():
    response = {
        "data": "good morning",
    }
    return jsonify(response)
