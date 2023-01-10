from flask import Flask
from app.urls import tasks
from flask_cors import CORS
app = Flask(__name__)

CORS(app,resources={r"/*": {"origins": "*"}}, headers="Content-Type", support_credentials=True)
app.register_blueprint(tasks)

if __name__ == '__main__':  
  app.run(host='0.0.0.0', port=8080, debug=True)