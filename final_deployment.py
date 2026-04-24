import joblib
import pandas as pd
from flask import Flask, request, jsonify
from pyngrok import ngrok

app = Flask(__name__)

# Load your trained model and scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return "Furniture Price Prediction API is Live!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the friend's request
        data = request.get_json()
        df = pd.DataFrame(data)
        
        # Scaling and Prediction logic from your notebook
        features_scaled = scaler.transform(df)
        prediction = model.predict(features_scaled)
        
        return jsonify({
            'status': 'success',
            'suggested_online_price': round(float(prediction[0]), 2),
            'currency': 'INR'
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    # 1. Start Ngrok Tunnel (Make sure your auth token is set in your environment)
    public_url = ngrok.connect(5000).public_url
    print(f" * Public API URL: {public_url}")
    
    # 2. Run Flask App
    app.run(port=5000)