import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
import requests
import pickle
def fetch_weather_data(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data
api_key = 'a6673e782011461b31f86f49a5d71adb'
city_name = 'Kottayam'
weather_data = fetch_weather_data(city_name, api_key)
weather_features = {
    'Temperature': weather_data['main']['temp'],
    'Humidity': weather_data['main']['humidity'],
    'Wind Speed': weather_data['wind']['speed'],
    'Cloudiness': weather_data['clouds']['all']
}
weather_df = pd.DataFrame([weather_features])
is_cloud_burst = 1 if weather_data['weather'][0]['main'] == 'Rain' else 0
data_for_prediction = weather_df.copy()
data_for_prediction['IsCloudBurst'] = is_cloud_burst
with open('random_forest_model.pkl', 'rb') as f:
    rf_model = pickle.load(f)
try:
    with open('random_forest_model.pkl', 'rb') as f:
        rf_model = pickle.load(f)
except EOFError:
    print("Error: The pickle file is empty or corrupted.")
with open('random_forest_model_and_data.pkl', 'rb') as f:
    model_and_data = pickle.load(f)
rf_model = model_and_data['model']
X_train = model_and_data['X_train']
y_train = model_and_data['y_train']
training_columns = X_train.columns
data_for_prediction = data_for_prediction.reindex(columns=training_columns, fill_value=0)
prediction = rf_model.predict(data_for_prediction)
if prediction[0] == 1:
    print("Cloud burst is predicted in the specified location.")
else:
    print("No cloud burst is predicted in the specified location.")