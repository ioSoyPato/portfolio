# Create a ticket price prediction model (Airline)

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import streamlit as st
from datetime import datetime, timedelta

def load_data():
    try:
        df = pd.read_csv('airline_price.csv')
        return df
    except Exception as e:
        # Generate random data with patterns for demonstration
        np.random.seed(42)  # For reproducible results
        size = 1000
        
        # Create base data
        df = pd.DataFrame({
            'origin': np.random.choice(['NYC', 'LAX', 'CHI', 'MIA', 'SFO'], size=size),
            'destination': np.random.choice(['LON', 'PAR', 'TOK', 'MEX', 'MAD'], size=size),
            'day_of_week': np.random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], size=size),
            'hour': np.random.randint(0, 24, size=size),
            'distance': np.random.uniform(500, 5000, size=size),
        })
        
        # Add price with patterns
        base_price = 500
        df['price'] = base_price + \
                     df['distance'] * 0.1 + \
                     np.where(df['day_of_week'].isin(['Saturday', 'Sunday']), 100, 0) + \
                     np.where(df['hour'].between(6, 9), 50, 0) + \
                     np.where(df['hour'].between(17, 20), 75, 0) + \
                     np.random.normal(0, 50, size=size)
        
        return df

def analyze_best_times(df, origin, destination):
    # Filter for specific route
    route_data = df[
        (df['origin'] == origin) & 
        (df['destination'] == destination)
    ].copy()
    
    if len(route_data) == 0:
        return None, None
    
    # Analyze best day of week
    day_analysis = route_data.groupby('day_of_week')['price'].agg(['mean', 'count']).round(2)
    best_day = day_analysis['mean'].idxmin()
    
    # Analyze best hour
    hour_analysis = route_data.groupby('hour')['price'].mean()
    best_hour = hour_analysis.idxmin()
    
    return best_day, best_hour

def show_project():
    st.markdown("""
        <div class="project-card">
            <h1>Flight Price Optimizer</h1>
            <p>Find the best time to book your flights and save money!</p>
        </div>
    """, unsafe_allow_html=True)

    # Load data
    df = load_data()
    
    # Create input columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div class="project-card">
                <h3>Origin</h3>
            </div>
        """, unsafe_allow_html=True)
        origin = st.selectbox(
            "Select departure city",
            sorted(df['origin'].unique())
        )
    
    with col2:
        st.markdown("""
            <div class="project-card">
                <h3>Destination</h3>
            </div>
        """, unsafe_allow_html=True)
        destination = st.selectbox(
            "Select arrival city",
            sorted(df['destination'].unique())
        )

    if st.button("Analyze Best Times", use_container_width=True):
        best_day, best_hour = analyze_best_times(df, origin, destination)
        
        if best_day is None:
            st.error("No data available for this route.")
            return
        
        # Display recommendations
        st.markdown(f"""
            <div class="project-card">
                <h2>Booking Recommendations</h2>
                <div style="text-align: center;">
                    <h3>✈️ {origin} → {destination}</h3>
                    <p>Based on our analysis of historical prices:</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
                <div class="project-card">
                    <h3>Best Day to Book</h3>
                    <h2 style="color: #2E4057; text-align: center;">{best_day}</h2>
                </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
                <div class="project-card">
                    <h3>Best Time to Book</h3>
                    <h2 style="color: #2E4057; text-align: center;">{best_hour:02d}:00</h2>
                </div>
            """, unsafe_allow_html=True)

        # Show price trends
        st.markdown("""
            <div class="project-card">
                <h3>Price Trends</h3>
            </div>
        """, unsafe_allow_html=True)
        
        # Create two columns for day and hour trends
        col1, col2 = st.columns(2)
        
        with col1:
            # Day of week price trend
            route_data = df[(df['origin'] == origin) & (df['destination'] == destination)]
            day_prices = route_data.groupby('day_of_week')['price'].mean()
            
            fig1, ax1 = plt.subplots(figsize=(8, 4))
            day_prices.plot(kind='bar', ax=ax1)
            plt.title('Average Prices by Day of Week')
            plt.xticks(rotation=45)
            plt.ylabel('Price ($)')
            st.pyplot(fig1)
        
        with col2:
            # Hour price trend
            hour_prices = route_data.groupby('hour')['price'].mean()
            
            fig2, ax2 = plt.subplots(figsize=(8, 4))
            hour_prices.plot(kind='line', ax=ax2)
            plt.title('Average Prices by Hour')
            plt.xlabel('Hour of Day')
            plt.ylabel('Price ($)')
            st.pyplot(fig2)

        # Additional tips
        st.markdown("""
            <div class="project-card">
                <h3>💡 Booking Tips</h3>
                <ul>
                    <li>Book at least 6 weeks in advance for best prices</li>
                    <li>Mid-week flights tend to be cheaper</li>
                    <li>Early morning or late-night flights often have better rates</li>
                    <li>Prices tend to be higher during holidays and peak seasons</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    show_project()