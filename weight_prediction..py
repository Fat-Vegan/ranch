import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Simulated cattle data
data = pd.DataFrame({
    'age_months': [6, 12, 18, 24, 30],
    'feed_intake_kg': [15, 20, 25, 30, 35],
    'weight_kg': [200, 350, 500, 650, 800]
})

# Train linear regression model
X = data[['age_months', 'feed_intake_kg']]
y = data['weight_kg']
model = LinearRegression()
model.fit(X, y)

# Predict weight for new cattle
new_cattle = pd.DataFrame({'age_months': [15], 'feed_intake_kg': [22]})
predicted_weight = model.predict(new_cattle)
print(f"Predicted Weight: {predicted_weight[0]:.2f} kg")

# Visualize
plt.scatter(data['age_months'], data['weight_kg'], color='blue', label='Actual')
plt.plot(data['age_months'], model.predict(X), color='red', label='Predicted')
plt.xlabel('Age (Months)')
plt.ylabel('Weight (kg)')
plt.legend()
plt.show()
