import numpy as np
import pickle
import streamlit as st

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