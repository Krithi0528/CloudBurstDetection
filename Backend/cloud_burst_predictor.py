# cloud_burst_predictor.py

import pandas as pd
import requests
import pickle
from sklearn.base import BaseEstimator

class CloudBurstPredictor(BaseEstimator):
    def __init__(self):
        pass
    def fetch_weather_data(self, city_name, api_key):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        return data
    
    def predict_cloud_burst(self, location):
        api_key = 'a6673e782011461b31f86f49a5d71adb'
        weather_data = self.fetch_weather_data(location, api_key)
        
        # Process weather data to create features
        weather_features = {
            'Temperature': weather_data['main']['temp'],
            'Humidity': weather_data['main']['humidity'],
            'Wind Speed': weather_data['wind']['speed'],
            'Cloudiness': weather_data['clouds']['all']
        }
        weather_df = pd.DataFrame([weather_features])
        
        # Load the trained model
        with open('random_forest_model.pkl', 'rb') as f:
            rf_model = pickle.load(f)
        
        # Make predictions using the loaded model
        prediction = rf_model.predict(weather_df)
        
        # Return the prediction result
        if prediction[0] == 1:
            return "Cloud burst is predicted in the specified location."
        else:
            return "No cloud burst is predicted in the specified location."
