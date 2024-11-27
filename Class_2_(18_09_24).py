import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import streamlit as st

# Load dataset
energy_data = pd.read_csv('energy_dataset.csv')

# Convert 'time' column to datetime and remove timezone information
energy_data['time'] = pd.to_datetime(energy_data['time'], utc=True).dt.tz_localize(None)

# Add temporal features
energy_data['hour'] = energy_data['time'].dt.hour
energy_data['day_of_week'] = energy_data['time'].dt.dayofweek
energy_data['month'] = energy_data['time'].dt.month
energy_data['year'] = energy_data['time'].dt.year

# Group renewable and fossil energy generation
renewable_sources = [
    'generation biomass',
    'generation hydro run-of-river and poundage',
    'generation hydro water reservoir',
    'generation marine',
    'generation solar',
    'generation wind offshore',
    'generation wind onshore',
    'generation other renewable'
]

fossil_sources = [
    'generation fossil brown coal/lignite',
    'generation fossil coal-derived gas',
    'generation fossil gas',
    'generation fossil hard coal',
    'generation fossil oil',
    'generation fossil oil shale',
    'generation fossil peat'
]

energy_data['renewable_generation'] = energy_data[renewable_sources].sum(axis=1)
energy_data['fossil_generation'] = energy_data[fossil_sources].sum(axis=1)

# Prepare data for modeling
model_data = energy_data[
    [
        'total load actual',
        'total load forecast',
        'renewable_generation',
        'fossil_generation',
        'hour',
        'day_of_week',
        'month',
        'price day ahead',
        'price actual'
    ]
].dropna()

# Define features (X) and target (y)
X = model_data.drop(columns=['total load actual'])
y = model_data['total load actual']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print metrics
print(f"Mean Squared Error: {mse}")
print(f"R² Score: {r2}")

# Streamlit Application
st.title('Energy Demand Forecasting App')

# File upload section
uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])

if uploaded_file:
    # Read the uploaded file
    new_data = pd.read_csv(uploaded_file)

    # Feature engineering on new data
    new_data['time'] = pd.to_datetime(new_data['time'], utc=True).dt.tz_localize(None)
    new_data['hour'] = new_data['time'].dt.hour
    new_data['day_of_week'] = new_data['time'].dt.dayofweek
    new_data['month'] = new_data['time'].dt.month
    new_data['renewable_generation'] = new_data[renewable_sources].sum(axis=1)
    new_data['fossil_generation'] = new_data[fossil_sources].sum(axis=1)

    # Select relevant features for prediction
    features = new_data[['total load forecast', 'renewable_generation', 'fossil_generation',
                         'hour', 'day_of_week', 'month', 'price day ahead', 'price actual']]

    # Make predictions
    predictions = model.predict(features)

    # Display predictions
    new_data['Predicted Load'] = predictions
    st.write(new_data[['time', 'Predicted Load']])

    # Download predictions
    csv = new_data.to_csv(index=False).encode('utf-8')
    st.download_button("Download Predictions", data=csv, file_name="predictions.csv")
