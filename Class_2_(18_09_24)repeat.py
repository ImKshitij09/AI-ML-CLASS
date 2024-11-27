import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Title of the Streamlit app
st.title("Interactive Energy Demand Forecasting App")

# Section 1: Upload Dataset
st.header("Step 1: Upload Dataset")
uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])

if uploaded_file:
    # Load the dataset
    energy_data = pd.read_csv(uploaded_file)

    # Display a preview of the dataset
    st.subheader("Dataset Preview")
    st.write(energy_data.head())

    # Convert 'time' column to datetime and add temporal features
    energy_data['time'] = pd.to_datetime(energy_data['time'], utc=True).dt.tz_localize(None)
    energy_data['hour'] = energy_data['time'].dt.hour
    energy_data['day_of_week'] = energy_data['time'].dt.dayofweek
    energy_data['month'] = energy_data['time'].dt.month

    # Aggregate renewable and fossil energy generation
    renewable_sources = [
        'generation biomass', 'generation hydro run-of-river and poundage',
        'generation hydro water reservoir', 'generation marine', 'generation solar',
        'generation wind offshore', 'generation wind onshore', 'generation other renewable'
    ]
    fossil_sources = [
        'generation fossil brown coal/lignite', 'generation fossil coal-derived gas',
        'generation fossil gas', 'generation fossil hard coal', 'generation fossil oil',
        'generation fossil oil shale', 'generation fossil peat'
    ]
    energy_data['renewable_generation'] = energy_data[renewable_sources].sum(axis=1)
    energy_data['fossil_generation'] = energy_data[fossil_sources].sum(axis=1)

    # Section 2: Data Visualization
    st.header("Step 2: Data Visualization")

    # Renewable vs Fossil Energy
    st.subheader("Total Renewable vs Fossil Energy Generation")
    fig, ax = plt.subplots()
    ax.bar(['Renewable', 'Fossil'], [
        energy_data['renewable_generation'].sum(),
        energy_data['fossil_generation'].sum()
    ])
    st.pyplot(fig)

    # Time-series of energy generation
    st.subheader("Energy Generation Over Time")
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(energy_data['time'], energy_data['renewable_generation'], label='Renewable')
    ax.plot(energy_data['time'], energy_data['fossil_generation'], label='Fossil')
    ax.legend()
    st.pyplot(fig)

    # Section 3: Train and Predict
    st.header("Step 3: Train and Predict")

    # Prepare data for training
    model_data = energy_data[
        ['total load actual', 'total load forecast', 'renewable_generation', 'fossil_generation',
         'hour', 'day_of_week', 'month', 'price day ahead', 'price actual']
    ].dropna()

    X = model_data.drop(columns=['total load actual'])
    y = model_data['total load actual']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Display metrics
    st.subheader("Model Performance")
    st.write(f"Mean Squared Error (MSE): {mse}")
    st.write(f"R² Score: {r2}")

    # Allow the user to make predictions
    st.subheader("Make Predictions on New Data")
    if st.checkbox("Use uploaded dataset for predictions?"):
        features = X_test
        predictions = model.predict(features)

        # Display predictions
        predictions_df = pd.DataFrame({
            "Time": energy_data['time'].iloc[features.index],
            "Predicted Load": predictions
        })
        st.write(predictions_df)

        # Download predictions
        csv = predictions_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Predictions as CSV", data=csv, file_name="predictions.csv")
