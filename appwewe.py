import streamlit as st
import pandas as pd
import joblib
import os

# Load the trained model
model_path = '/content/energy_forecasting_model.pkl'  # Update to Colab's file path
model = joblib.load(model_path)

# Define the Streamlit app
def app():
    st.title("Energy Demand Forecasting App")

    st.header("Input Features")
    # Create input fields for features
    total_load_forecast = st.number_input("Total Load Forecast (MW)")
    renewable_generation = st.number_input("Renewable Generation (MW)")
    fossil_generation = st.number_input("Fossil Generation (MW)")
    price_actual = st.number_input("Price Actual (€/MWh)")
    price_day_ahead = st.number_input("Price Day Ahead (€/MWh)")
    hour = st.number_input("Hour of Day (0-23)", min_value=0, max_value=23, step=1)
    day_of_week = st.number_input("Day of Week (0=Monday, 6=Sunday)", min_value=0, max_value=6, step=1)
    month = st.number_input("Month (1-12)", min_value=1, max_value=12, step=1)

    # Prepare input data
    input_data = pd.DataFrame({
        'total load forecast': [total_load_forecast],
        'renewable_generation': [renewable_generation],
        'fossil_generation': [fossil_generation],
        'price actual': [price_actual],
        'price day ahead': [price_day_ahead],
        'hour': [hour],
        'day_of_week': [day_of_week],
        'month': [month]
    })

    # Predict button
    if st.button("Predict"):
        prediction = model.predict(input_data)[0]
        st.success(f"Predicted Total Load: {prediction:,.2f} MW")

# Run the app
if __name__ == "__main__":
    app()
