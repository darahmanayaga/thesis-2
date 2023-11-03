import numpy as np
import pickle
import streamlit as st

import tensorflow as tf

# Print the TensorFlow version in your Streamlit app
print("TensorFlow version in Streamlit app:", tf.__version__)

# Load the saved model
loaded_model = pickle.load(open('trained_hybrid_model.sav', 'rb'))

def coffee_prediction(input_data):

    input_data_as_numpy_array = np.asarray(input_data)

    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)

    return f"Predicted output: {prediction}"



def main():

    # Website title
    st.title('Coffee Yield Prediction Web App')

    # Getting input data from the user
    weathercode = st.text_input('Weathercode')
    temperature_2m = st.text_input('Temperature in °C')
    relativehumidity_2m = st.text_input('Relative Humidity')
    dewpoint_2m = st.text_input('Dewpoint in °C')
    rain = st.text_input('Rain')
    surface_pressure = st.text_input('Surface Pressure')
    cloudcover = st.text_input('Cloudcover')
    et0_fao_evapotranspiration = st.text_input('Evapotranspiration')
    vapor_pressure_deficit = st.text_input("Vapor Pressure Deficit")
    Wind_Direction = st.text_input("Wind Direction")
    Wind_Speed = st.text_input("Wind Speed")
    windgusts_10m = st.text_input("Windgusts")
    soil_temperature_28_to_100cm = st.text_input("Soil Temperature in °C")
    soil_moisture_28_to_100cm = st.text_input("Soil Moisture")
    direct_radiation = st.text_input("Direct Radiation")
    diffuse_radiation = st.text_input("Diffuse Radiation")

    # Code for prediction
    Yield = ''

    # Button for prediction
    if st.button('Predict Coffee Yield'):
        Yield = coffee_prediction([weathercode,temperature_2m,relativehumidity_2m,dewpoint_2m,
                                    rain,surface_pressure,cloudcover,et0_fao_evapotranspiration,
                                    vapor_pressure_deficit,Wind_Direction,Wind_Speed,windgusts_10m,
                                    soil_temperature_28_to_100cm,soil_moisture_28_to_100cm,
                                    direct_radiation,diffuse_radiation])
    
    st.success(Yield)



if __name__ == '__main__':
    main()