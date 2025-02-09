import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from datetime import datetime, timedelta

def train_arima_model(historical_data):
    """
    Train an ARIMA model on historical weather data.
    :param historical_data: Pandas DataFrame with columns ['date', 'temperature'].
    :return: Trained ARIMA model.
    """
    # Convert date column to datetime and set as index
    historical_data['date'] = pd.to_datetime(historical_data['date'])
    historical_data.set_index('date', inplace=True)

    # Fit ARIMA model
    model = ARIMA(historical_data['temperature'], order=(5, 1, 0))  # (p, d, q) parameters
    fitted_model = model.fit()
    return fitted_model

def predict_temperature(model, start_date, periods=7):
    """
    Predict temperature for future dates using the trained ARIMA model.
    :param model: Trained ARIMA model.
    :param start_date: Start date for prediction (datetime object).
    :param periods: Number of days to predict.
    :return: List of predicted temperatures.
    """
    # Generate future dates
    future_dates = [start_date + timedelta(days=i) for i in range(periods)]

    # Predict temperatures
    forecast = model.forecast(steps=periods)
    predictions = list(forecast)

    return future_dates, predictions