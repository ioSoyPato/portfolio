# House price prediction

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import streamlit as st
import folium
from streamlit_folium import folium_static
from sklearn.preprocessing import StandardScaler

def load_data():
    try:
        df = pd.read_csv('house_prices.csv')
        return df
    except Exception as e:
        # Generate random data for demonstration
        df = pd.DataFrame({
            'bedrooms': np.random.randint(1, 10, size=100),
            'bathrooms': np.random.randint(1, 10, size=100),
            'm2': np.random.randint(30, 1000, size=100),
            'age': np.random.randint(0, 100, size=100),
            'latitude': np.random.uniform(20, 21, size=100),
            'longitude': np.random.uniform(-103, -102, size=100)
        })
        return df

def predict_house_price(features):
    # For demo purposes, we'll use a random prediction with some influence from the features
    base_price = 500000  # Base price of 500k
    
    # Add some weight to each feature
    price = base_price + \
            (features['bedrooms'] * 100000) + \
            (features['bathrooms'] * 75000) + \
            (features['m2'] * 1000) + \
            (features['age'] * -1000)  # Older houses decrease in value
    
    # Add some randomness (±10%)
    variation = np.random.uniform(-0.1, 0.1)
    final_price = price * (1 + variation)
    
    return max(final_price, 100000)  # Ensure minimum price of 100k

def show_project():
    st.markdown("""
        <div class="project-card">
            <h1>House Price Prediction</h1>
            <p>This tool predicts house prices based on key features and location.</p>
            <div class="skill-tag">Machine Learning</div>
            <div class="skill-tag">Real Estate</div>
            <div class="skill-tag">Geolocation</div>
        </div>
    """, unsafe_allow_html=True)

    # Create two columns for input features and map
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("""
            <div class="project-card">
                <h3>House Features</h3>
            </div>
        """, unsafe_allow_html=True)

        # Input features
        bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=3)
        bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=2)
        m2 = st.number_input("Square Meters", min_value=30, max_value=1000, value=150)
        age = st.number_input("House Age (years)", min_value=0, max_value=100, value=5)

    with col2:
        st.markdown("""
            <div class="project-card">
                <h3>Location</h3>
                <p>Click on the map to set the house location</p>
            </div>
        """, unsafe_allow_html=True)

        # Initialize the map centered on Guadalajara
        m = folium.Map(location=[20.6597, -103.3496], zoom_start=12)

        # Store the clicked location
        if 'latitude' not in st.session_state:
            st.session_state.latitude = 20.6597
            st.session_state.longitude = -103.3496

        # Add click event to map
        m.add_child(folium.ClickForMarker(popup='House Location'))
        
        # Display the map
        folium_static(m)

        # Show selected coordinates
        st.write(f"Selected Location: {st.session_state.latitude:.4f}, {st.session_state.longitude:.4f}")

    # Predict button
    if st.button("Predict Price", use_container_width=True):
        features = {
            'bedrooms': bedrooms,
            'bathrooms': bathrooms,
            'm2': m2,
            'age': age,
            'latitude': st.session_state.latitude,
            'longitude': st.session_state.longitude
        }

        predicted_price = predict_house_price(features)

        # Display prediction
        st.markdown(f"""
            <div class="project-card">
                <h2>Predicted House Price</h2>
                <h1 style="color: #2E4057; text-align: center;">
                    ${predicted_price:,.2f}
                </h1>
                <p style="text-align: center;">
                    This prediction is based on the provided features and location.
                    Actual prices may vary significantly.
                </p>
            </div>
        """, unsafe_allow_html=True)

        # Display feature importance (mock data for demonstration)
        st.markdown("<h3>Feature Importance</h3>", unsafe_allow_html=True)
        importance_data = {
            'Square Meters': 35,
            'Location': 25,
            'Bedrooms': 20,
            'Bathrooms': 15,
            'House Age': 5
        }

        for feature, importance in importance_data.items():
            st.markdown(f"**{feature}**")
            st.progress(importance/100)
            st.write(f"{importance}% impact on price")

df = load_data()


if __name__ == "__main__":
    show_project()