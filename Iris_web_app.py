import streamlit as st
import joblib
import pandas as pd

# Load the trained model and scaler
rf_model = joblib.load('rf_model.pkl')
scaler = joblib.load('scaler.pkl')

# Streamlit app
st.title("Iris Species Prediction")

st.sidebar.header("Input Features")

def user_input_features():
    sepal_length = st.sidebar.text_input("Sepal Length (cm)", "")
    sepal_width = st.sidebar.text_input("Sepal Width (cm)", "")
    petal_length = st.sidebar.text_input("Petal Length (cm)", "")
    petal_width = st.sidebar.text_input("Petal Width (cm)", "")
    
    # Convert inputs to a dictionary if they are all provided
    if sepal_length and sepal_width and petal_length and petal_width:
        data = {
            'SepalLengthCm': [float(sepal_length)],
            'SepalWidthCm': [float(sepal_width)],
            'PetalLengthCm': [float(petal_length)],
            'PetalWidthCm': [float(petal_width)]
        }
        features = pd.DataFrame(data)
        return features
    return None

input_df = user_input_features()

if input_df is not None:
    # Preprocess the input features
    input_scaled = scaler.transform(input_df)

    # Make predictions
    prediction = rf_model.predict(input_scaled)
    prediction_proba = rf_model.predict_proba(input_scaled)

    st.subheader("Prediction")
    st.write(prediction[0])

    st.subheader("Prediction Probability")
    st.write(prediction_proba)

    st.subheader("Input Features")
    st.write(input_df)
else:
    st.write("Please provide all input features to make a prediction.")
