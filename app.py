import streamlit as st
import pandas as pd
import joblib
import numpy as np

# --- Loading the Final, Simplified Pipeline and Data ---
try:
    # Loading the single, complete pipeline file trained on core features
    pipeline = joblib.load('models/final_full_pipeline.joblib')
    # Loading the clean data to get dropdown options
    df_clean = pd.read_csv('data/processed/cleaned_laptops.csv')
except FileNotFoundError:
    st.error("Error: Model pipeline not found. Please run all training notebooks again.")
    st.stop()


# --- Setting Up the Web App's User Interface ---
st.set_page_config(page_title="Laptop Price Analyzer", layout="wide")
st.title('💻 Laptop Price Analyzer')
st.write("This interactive app predicts the market price of a laptop based on its core specifications.")
st.write("---")


# --- Creating a Simple and Clean Input Form ---
st.header("Enter Laptop Specifications")

# Using a single column for a focused user experience
ram_gb = st.selectbox('RAM (in GB)', options=sorted(df_clean['ram_gb'].unique()))
ssd_gb = st.selectbox('SSD Storage (in GB)', options=sorted(df_clean['ssd_gb'].unique()))
screen_size_inch = st.selectbox('Screen Size (in Inches)', options=sorted(df_clean['screen_size_inch'].unique()))
processor_brand = st.selectbox('Processor Brand', options=sorted(df_clean['processor_brand'].unique()))


# --- Prediction Logic ---
if st.button('Analyze and Predict Price', key='predict_button'):
    
    # 1. Creating a DataFrame from the user's input with the 4 core features
    input_df = pd.DataFrame([{
        'ram_gb': ram_gb,
        'ssd_gb': ssd_gb,
        'screen_size_inch': screen_size_inch,
        'processor_brand': processor_brand
    }])

    # 2. The pipeline handles all preprocessing and prediction in one step
    predicted_log_price = pipeline.predict(input_df)[0]
    
    # 3. Converting the prediction back from the log scale
    predicted_price = np.expm1(predicted_log_price)

    # 4. Displaying the final, correct result
    st.write("---")
    st.subheader('Predicted Market Price:')
    st.success(f'## ₹ {predicted_price:,.2f}')