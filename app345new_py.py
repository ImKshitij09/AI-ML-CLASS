import os
import streamlit as st
import joblib
import pandas as pd
import numpy as np
import time

# Load pre-trained model
model_path = "energy_forecasting_model.pkl"
try:
    model = joblib.load(model_path)
except FileNotFoundError:
    model = None
    st.error("Model file not found! Please upload the trained model.")

# Define the Streamlit app
def app():
    st.title("🌟 Energy Demand and Price Prediction App")
    st.markdown("This app predicts **total energy load** and **price forecasts** based on user inputs.")

    # Tabs for Input and Output
    tab1, tab2 = st.tabs(["⚙️ Input Features", "📊 Prediction Results"])

    # Input Features Tab
    with tab1:
        st.subheader("Provide the following details:")
        col1, col2 = st.columns(2)

        with col1:
            total_load_forecast = st.slider("Total Load Forecast (MW)", min_value=0.0, max_value=1000.0, value=0.0, step=0.1)
            renewable_generation = st.slider("Renewable Generation (MW)", min_value=0.0, max_value=1000.0, value=0.0, step=0.1)
            hour = st.slider("Hour of Day (0-23)", min_value=0, max_value=23, value=12, step=1)

        with col2:
            price_day_ahead = st.slider("Price Day Ahead (€/MWh)", min_value=0.0, max_value=500.0, value=0.0, step=0.1)
            fossil_generation = st.slider("Fossil Generation (MW)", min_value=0.0, max_value=1000.0, value=0.0, step=0.1)
            price_actual = st.slider("Price Actual (€/MWh)", min_value=0.0, max_value=500.0, value=0.0, step=0.1)
            
            day_of_week = st.selectbox("Day of Week", options=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], index=0)

        # Mapping the day_of_week to integer (0 for Monday, 6 for Sunday)
        day_of_week_mapping = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
        day_of_week_index = day_of_week_mapping.get(day_of_week, 0)

        # Month input
        month = st.selectbox("Month", options=list(range(1, 13)), format_func=lambda x: f"Month {x}")

        # Summary of Input Features
        st.markdown("### Summary of Input Features")
        st.write({
            "Total Load Forecast": total_load_forecast,
            "Renewable Generation": renewable_generation,
            "Fossil Generation": fossil_generation,
            "Price Actual": price_actual,
            "Price Day Ahead": price_day_ahead,
            "Hour": hour,
            "Day of Week": day_of_week,
            "Month": month,
        })

    # Prediction Results Tab
    with tab2:
        st.subheader("Results")
        if st.button("Predict"):
            if model:
                # Prepare input data for prediction
                input_data = pd.DataFrame({
                    'total load forecast': [total_load_forecast],
                    'renewable_generation': [renewable_generation],
                    'fossil_generation': [fossil_generation],
                    'price actual': [price_actual],
                    'price day ahead': [price_day_ahead],
                    'hour': [hour],
                    'day_of_week': [day_of_week_index],  # Using the integer value for day_of_week
                    'month': [month]
                })

                # Model prediction
                try:
                    prediction = model.predict(input_data)[0]
                    st.success(f"Predicted Total Load: {prediction:,.2f} MW")
                    st.balloons()
                except Exception as e:
                    st.error(f"Prediction failed: {e}")
            else:
                st.error("Prediction failed. Model not loaded.")

# Run the app
if __name__ == "__main__":
    app()
