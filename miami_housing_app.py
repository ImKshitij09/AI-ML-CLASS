import streamlit as st
import joblib
import pandas as pd
import numpy as np
import os
import time
import folium
import streamlit_folium as st_folium  # Import streamlit_folium for Folium integratio   

# Load the model
model_path = os.path.join(os.path.dirname(__file__), 'miami_housing_model')  # Replace with your actual model file name
model = joblib.load(model_path)

# Define the Streamlit app
def app():
    # Set up the title
    st.title("Miami Housing Price Prediction")
    
    # Create input fields for various features
    latitude = st.number_input("Latitude", value=latitude)
    longitude = st.number_input("Longitude", value=longitude)
    lnd_sqfoot = st.number_input("Land Square Footage")
    tot_lvg_area = st.number_input("Total Living Area")
    spec_feat_val = st.number_input("Special Feature Value")
    rail_dist = st.number_input("Distance to Rail")
    ocean_dist = st.number_input("Distance to Ocean")
    water_dist = st.number_input("Distance to Water")
    cntr_dist = st.number_input("Distance to Center")
    subcntr_di = st.number_input("Distance to Subcenter")
    hwy_dist = st.number_input("Distance to Highway")
    age = st.number_input("Age of House")
    avno60plus = st.number_input("Number of Avenues over 60 feet wide")
    month_sold = st.number_input("Month Sold")
    structure_quality = st.number_input("Structure Quality")

    # Create a dataframe from the input values
    input_data = pd.DataFrame({
        'LATITUDE': [latitude],
        'LONGITUDE': [longitude],
        'LND_SQFOOT': [lnd_sqfoot],
        'TOT_LVG_AREA': [tot_lvg_area],
        'SPEC_FEAT_VAL': [spec_feat_val],
        'RAIL_DIST': [rail_dist],
        'OCEAN_DIST': [ocean_dist],
        'WATER_DIST': [water_dist],
        'CNTR_DIST': [cntr_dist],
        'SUBCNTR_DI': [subcntr_di],
        'HWY_DIST': [hwy_dist],
        'age': [age],
        'avno60plus': [avno60plus],
        'month_sold': [month_sold],
        'structure_quality': [structure_quality]
    })

    # Predict the housing price on button click
    if st.button("Predict"):
        with st.spinner('Calculating...'):  # Display a spinner while predicting
            time.sleep(1)  # Simulate some processing time
            prediction = model.predict(input_data)[0]
            st.success(f"Predicted Price: ${prediction:,.2f}")  # Display the predicted price
            st.balloons()  # Show balloons after prediction

# Run the app
if __name__ == "__main__":
    app()
