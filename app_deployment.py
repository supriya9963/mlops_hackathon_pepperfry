from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    query_df = pd.DataFrame(data)
    prediction = model.predict(query_df)
    return jsonify({'suggested_price': list(prediction)})

if __name__ == '__main__':
    app.run(port=5000, debug=True)