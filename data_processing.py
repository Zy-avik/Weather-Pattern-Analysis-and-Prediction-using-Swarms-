import pandas as pd
from datetime import datetime, timedelta
import random

def generate_historical_data(location, days=365):
    """
    Generate simulated historical weather data for a location.
    :param location: Location name (str).
    :param days: Number of days of historical data to generate.
    :return: Pandas DataFrame with columns ['date', 'temperature'].
    """
    start_date = datetime.now() - timedelta(days=days)
    dates = [start_date + timedelta(days=i) for i in range(days)]
    temperatures = [random.uniform(10, 30) for _ in range(days)]  # Simulated temperatures

    historical_data = pd.DataFrame({
        'date': dates,
        'temperature': temperatures
    })
    return historical_data