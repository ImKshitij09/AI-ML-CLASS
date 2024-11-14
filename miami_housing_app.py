import streamlit as st
import joblib
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import os
import time
import streamlit_folium as st_folium  # Import streamlit_folium
import folium  # Import folium for map creation

# Load the model
model_path = os.path.join(os.path.dirname(__file__), 'miami_housing_model') # replace miami_housing_model with the actual file name
model = joblib.load(model_path)

# Define the Streamlit app
def app():
  st.title("Miami Housing Price Prediction")
   # Create a map
    m = folium.Map(location=[25.7617, -80.1918], zoom_start=10)  # Centered on Miami

    # Add a marker that can be dragged
    marker = folium.Marker(
        location=[25.7617, -80.1918],  # Initial location
        draggable=True,
        popup="Drag me to select location",
    )
    marker.add_to(m)

    # Display the map
    map_data = st_folium.st_data(m)

    # Get the selected latitude and longitude from the map
    if map_data and map_data["last_object_clicked"]:
        latitude = map_data["last_object_clicked"]["lat"]
        longitude = map_data["last_object_clicked"]["lng"]
    else:
        latitude = 25.7617  # Default latitude
        longitude = -80.1918  # Default longitude

    # Display the selected coordinates
    st.write(f"Latitude: {latitude}, Longitude: {longitude}")


  # Create input fields for features
  latitude = st.number_input("Latitude")
  longitude = st.number_input("Longitude")
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
        'LATITUDE': [latitude],'LONGITUDE': [longitude], 
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
  if st.button("Predict"):
    with st.spinner('Calculating...'):  # Display a spinner while predicting
      time.sleep(1)  # Simulate some processing time
      prediction = model.predict(input_data)[0]
      st.success(f"Predicted Price: ${prediction:,.2f}")
      st.balloons()  # Show balloons after prediction

# Run the app
if __name__ == "__main__":
  app()
