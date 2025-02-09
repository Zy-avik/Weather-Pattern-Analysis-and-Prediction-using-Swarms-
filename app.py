from flask import Flask, request, jsonify
from data_processing import generate_historical_data
from arima_model import train_arima_model, predict_temperature
from datetime import datetime

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather():
    location = request.args.get('location')
    
    # Generate historical data for the location
    historical_data = generate_historical_data(location)
    
    # Train ARIMA model
    model = train_arima_model(historical_data)
    
    # Predict temperatures for the next 7 days
    start_date = datetime.now()
    future_dates, predictions = predict_temperature(model, start_date, periods=7)
    
    # Format response
    response = {
        'location': location,
        'forecast': [
            {'date': date.strftime('%Y-%m-%d'), 'temperature': round(temp, 2)}
            for date, temp in zip(future_dates, predictions)
        ]
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)