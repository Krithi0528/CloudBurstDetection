import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import requests
import pickle
def fetch_weather_data(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data
    cities = ['Uttarakhand', 'New York', 'London']
start_date = '2023-01-01'
end_date = '2023-01-05'
weather_data_list = []
is_cloud_burst_list = []
for city_name in cities:
    for date in pd.date_range(start=start_date, end=end_date):
        weather_data = fetch_weather_data(city_name, api_key)
        weather_features = {
            'Temperature': weather_data['main']['temp'],
            'Humidity': weather_data['main']['humidity'],
            'Wind Speed': weather_data['wind']['speed'],
            'Cloudiness': weather_data['clouds']['all']
        }
        weather_data_list.append(weather_features)
        is_cloud_burst = 1 if weather_data['weather'][0]['main'] == 'Rain' else 0
        is_cloud_burst_list.append(is_cloud_burst)
        weather_df = pd.DataFrame(weather_data_list)
        y = pd.Series(is_cloud_burst_list)
        X_train, X_test, y_train, y_test = train_test_split(weather_df, y, test_size=0.2, random_state=42)
        rf_model = RandomForestClassifier()
rf_model.fit(X_train, y_train)
with open('random_forest_model.pkl', 'wb') as f:
    pickle.dump(rf_model, f)
    with open('random_forest_model.pkl', 'rb') as f:
    rf_model = pickle.load(f)
    # Save the trained model and training data together
with open('random_forest_model_and_data.pkl', 'wb') as f:
    pickle.dump({'model': rf_model, 'X_train': X_train, 'y_train': y_train}, f)
    prediction = rf_model.predict(X_test)
    if prediction[0] == 1:
    print("Cloud burst is predicted in the specified location.")
else:
    print("No cloud burst is predicted in the specified location.")
    
