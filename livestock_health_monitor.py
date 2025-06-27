import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Simulated livestock sensor data (heart rate, activity)
data = pd.DataFrame({
    'animal_id': [1, 1, 1, 2, 2, 2],
    'heart_rate': [80, 85, 120, 78, 79, 80],
    'activity_level': [50, 55, 10, 60, 58, 59]
})

# Train Isolation Forest to detect anomalies
model = IsolationForest(contamination=0.1, random_state=42)
data['anomaly'] = model.fit_predict(data[['heart_rate', 'activity_level']])

# Flag anomalies (-1 indicates anomaly)
data['anomaly'] = data['anomaly'].apply(lambda x: 'Anomaly' if x == -1 else 'Normal')

# Visualize
plt.scatter(data['heart_rate'], data['activity_level'], c=data['anomaly'].map({'Normal': 'blue', 'Anomaly': 'red'}))
plt.xlabel('Heart Rate')
plt.ylabel('Activity Level')
plt.title('Livestock Health Anomaly Detection')
plt.show()

print(data)
