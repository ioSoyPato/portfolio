# Predict the temperature of a room based on the IOT data (temperature, humidity, etc.) // random data for now

import streamlit as st
import pandas as pd
import numpy as np


def predict_temperature(df):
    # Predict the temperature
    prediction = np.random.randint(20, 30)
    return prediction


def show_project():
    # Project Header with custom styling
    st.markdown("""
        <div class="project-card">
            <h1>Temperature Prediction</h1>
            <p>This project predicts the temperature of a room based on IoT sensor data including temperature, humidity, and other environmental factors.</p>
            <div class="skill-tag">Machine Learning</div>
            <div class="skill-tag">IoT</div>
            <div class="skill-tag">Data Analysis</div>
        </div>
    """, unsafe_allow_html=True)
    
    # File upload section
    st.markdown("""
        <div class="project-card">
            <h2>Upload Data</h2>
            <div class="uploadedFile">
                <p>Drag and drop your IoT sensor data file here</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    uploaded_file = st.file_uploader("", type=["csv", "CSV"])  # Label hidden as it's shown in HTML

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.markdown("""
                <div class="project-card">
                    <h2>IoT Data Preview</h2>
                    <p>Below is a preview of your uploaded sensor data:</p>
                </div>
            """, unsafe_allow_html=True)
            st.dataframe(df.head())

            # Prediction section
            col1, col2, col3 = st.columns([1,2,1])
            with col2:
                if st.button("Predict Temperature", use_container_width=True):
                    try:
                        prediction = predict_temperature(df)
                        st.markdown(f"""
                            <div class="success">
                                <h3>Prediction Result</h3>
                                <p>The predicted temperature is: {prediction}°C</p>
                            </div>
                        """, unsafe_allow_html=True)
                    except Exception as e:
                        st.markdown(f"""
                            <div class="error">
                                <h3>Error</h3>
                                <p>An error occurred during prediction: {str(e)}</p>
                            </div>
                        """, unsafe_allow_html=True)
        except Exception as e:
            st.markdown(f"""
                <div class="error">
                    <h3>Error</h3>
                    <p>Error reading the file: {str(e)}</p>
                    <p>Please ensure your file is a valid CSV format.</p>
                </div>
            """, unsafe_allow_html=True)

    # Add custom CSS for specific components
    st.markdown("""
        <style>
        .uploadedFile {
            margin: 2rem 0;
            padding: 2rem;
            background-color: #f8f9fa;
            border-radius: 8px;
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    show_project()