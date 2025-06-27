import pandas as pd
import requests

# Simulated pasture data
pastures = pd.DataFrame({
    'pasture_id': [1, 2, 3],
    'grass_quality': [0.8, 0.5, 0.9],  # 0 to 1 scale
    'area_acres': [50, 40, 60],
    'last_grazed': ['2025-06-01', '2025-06-10', '2025-05-20']
})

# Fetch weather data (example with OpenWeatherMap API)
def get_weather_forecast(city='YourCity', api_key='your_api_key'):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'
    response = requests.get(url).json()
    return response['list'][0]['weather'][0]['description']

# Simple grazing recommendation
def recommend_pasture(pastures):
    # Prioritize pastures with high grass quality and longer recovery time
    pastures['score'] = pastures['grass_quality'] * (pd.to_datetime('2025-06-27') - pd.to_datetime(pastures['last_grazed'])).dt.days
    return pastures.sort_values(by='score', ascending=False).iloc[0]

# Example usage
weather = get_weather_forecast()  # Replace with your API key
recommended = recommend_pasture(pastures)
print(f"Recommended Pasture: {recommended['pasture_id']}, Grass Quality: {recommended['grass_quality']}, Weather: {weather}")
