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

    return f"Predicted output: {prediction[0][0]:.2f}"



def main():

    # Website title
    st.title('Coffee Yield Prediction Web App')

    # Getting input data from the user
    weathercode =st.number_input('WMO Code')
    temp = st.number_input('Annual Average Temperature (°C)')
    rh = st.number_input('Annual Average Relative Humidity (%)')
    dp = st.number_input('Annual Average Dewpoint (°C)') 
    rain = st.number_input('Annual Total Rainfall (mm)') 
    sp = st.number_input('Annual Average Surface Pressure (hPa)') 
    cc= st.number_input('Annual Cloud Cover (%)') 
    evapo = st.number_input('Annual Average Evapotranspiration (mm)')
    vp = st.number_input('Annual Average Vapor Pressure Deficit (kPa)')
    wind_dir = st.number_input('Annual Prevailing Wind Direction') 
    wind_speed = st.number_input('Annual Prevailing Wind Speed (km/h)')
    wind_gust = st.number_input('Wind Gust (km/h)') 
    soil_temp = st.number_input('Annual Soil Temp (°C)') 
    soil_moist = st.number_input('Annual Average Soil Moist (m³/m³)') 
    dir_rad = st.number_input('Direct Radiation (W/m²)') 
    diff_rad = st.number_input('Diffuse Radiation (W/m²)') 

    # Code for prediction
    Yield = ''

    # Button for prediction
    if st.button('Predict Coffee Yield'):
        Yield = coffee_prediction([weathercode,temp,rh,dp,rain,sp,cc,evapo,vp,wind_dir,
        wind_speed,wind_gust,soil_temp,soil_moist,dir_rad,diff_rad])
    
    st.success(Yield)



if __name__ == '__main__':
    main()