# -*- coding: utf-8 -*-
"""app345new.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1s56zneCNovBbSHMbbdzmKGf7lQX0h_H5
"""

!pip install streamlit

import os
import streamlit as st
import joblib
import pandas as pd
import numpy as np
import os
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
            total_load_forecast = st.number_input("Total Load Forecast (MW)", value=0.0, step=0.1)
            renewable_generation = st.number_input("Renewable Generation (MW)", value=0.0, step=0.1)
            hour = st.slider("Hour of Day", 0, 23, value=12)

        with col2:
            fossil_generation = st.number_input("Fossil Generation (MW)", value=0.0, step=0.1)
            price_actual = st.number_input("Price Actual (€/MWh)", value=0.0, step=0.1)
            day_of_week = st.selectbox("Day of Week", options=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], index=0)

        month = st.selectbox("Month", options=list(range(1, 13)), format_func=lambda x: f"Month {x}")

        st.markdown("### Summary of Input Features")
        st.write({
            "Total Load Forecast": total_load_forecast,
            "Renewable Generation": renewable_generation,
            "Fossil Generation": fossil_generation,
            "Price Actual": price_actual,
            "Hour": hour,
            "Day of Week": day_of_week,
            "Month": month,
        })

    # Prediction Results Tab
    with tab2:
        st.subheader("Results")
        if st.button("Predict"):
            if model:
                # Prepare input data
                input_data = pd.DataFrame({
                    'total load forecast': [total_load_forecast],
                    'renewable_generation': [renewable_generation],
                    'fossil_generation': [fossil_generation],
                    'price actual': [price_actual],
                    'hour': [hour],
                    'day_of_week': [day_of_week],
                    'month': [month]
                })
                prediction = model.predict(input_data)[0]
                st.success(f"Predicted Total Load: {prediction:,.2f} MW")
                st.balloons()
            else:
                st.error("Prediction failed. Model not loaded.")

# Run the app
if __name__ == "__main__":
    app()