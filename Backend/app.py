# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from cloud_burst_predictor import CloudBurstPredictor

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000', 'http://localhost:3000'])

@app.route('/')
def index():
    return 'Welcome to the Cloud Burst Detection API!'

@app.route('/api/detect-cloud-burst', methods=['POST'])
def detect_cloud_burst_route():
    location = request.json.get('location')
    predictor = CloudBurstPredictor()
    result = predictor.predict_cloud_burst(location)
    return jsonify({'message': result})

if __name__ == '__main__':
    app.run(debug=True)
