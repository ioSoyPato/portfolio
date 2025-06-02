import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def show_project():
    # Add custom CSS class to title
    st.markdown("<h1>Regression Prediction Model</h1>", unsafe_allow_html=True)
    st.markdown("""
        <div class='project-card'>
            This project performs a regression prediction from a user-uploaded dataset.
            Follow the steps below to analyze your data.
        </div>
    """, unsafe_allow_html=True)
    
    # File upload with styled container
    st.markdown("<h2>Data Upload</h2>", unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="uploadedFile">', unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Upload your CSV", type=["csv","CSV"])
        st.markdown('</div>', unsafe_allow_html=True)
    
    target_column = st.text_input("Name of the column to predict (target):")
    
    if uploaded_file is not None and target_column:
        try:
            # Dataset display
            df = pd.read_csv(uploaded_file)
            st.markdown("<div class='success'>Dataset loaded successfully!</div>", unsafe_allow_html=True)
            st.dataframe(df.head())

            # Preprocessing section
            st.markdown("<h2>Data Preprocessing</h2>", unsafe_allow_html=True)
            df = preprocess_data(df, target_column)
            st.markdown("<div class='project-card'>", unsafe_allow_html=True)
            st.write("Processed data preview:")
            st.dataframe(df.head())
            st.markdown("</div>", unsafe_allow_html=True)

            # Dividir en variables independientes (X) y dependiente (y)
            X = df.drop(target_column, axis=1)
            y = df[target_column]

            # Dividir en conjunto de entrenamiento y prueba
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Entrenar modelo de regresión lineal
            model = LinearRegression()
            model.fit(X_train, y_train)

            # Evaluar el modelo
            predictions = model.predict(X_test)
            mse = mean_squared_error(y_test, predictions)
            r2 = r2_score(y_test, predictions)

            # Metrics display with styled cards
            st.markdown("<h2>Model Performance</h2>", unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"""
                    <div class='project-card'>
                        <h3>Mean Squared Error (MSE)</h3>
                        <h2>{mse:.2f}</h2>
                    </div>
                """, unsafe_allow_html=True)
            with col2:
                st.markdown(f"""
                    <div class='project-card'>
                        <h3>R² Score</h3>
                        <h2>{r2:.2f}</h2>
                    </div>
                """, unsafe_allow_html=True)

            # Predictions section
            st.markdown("<h2>Make Predictions</h2>", unsafe_allow_html=True)
            st.markdown('<div class="uploadedFile">', unsafe_allow_html=True)
            uploaded_new_data = st.file_uploader("Upload a CSV with the new data (without target column)", type=["csv"])
            st.markdown('</div>', unsafe_allow_html=True)

            if uploaded_new_data is not None:
                try:
                    new_data = pd.read_csv(uploaded_new_data)
                    st.markdown("<div class='success'>New data loaded successfully!</div>", unsafe_allow_html=True)
                    st.dataframe(new_data)
                    new_data = preprocess_data(new_data, target_column)
                    new_data[f"{target_column} predictions"] = model.predict(new_data)
                    st.markdown("<div class='project-card'>", unsafe_allow_html=True)
                    st.write("Predictions:")
                    st.dataframe(new_data)
                    st.markdown("</div>", unsafe_allow_html=True)
                except Exception as e:
                    st.markdown(f"<div class='error'>Error processing new data: {str(e)}</div>", unsafe_allow_html=True)
        except Exception as e:
            st.markdown(f"<div class='error'>Error processing data: {str(e)}</div>", unsafe_allow_html=True)

def preprocess_data(df, target_column):
    # Procesar datos categóricos con LabelEncoder
    le = LabelEncoder()
    for column in df.columns:
        if column != target_column and df[column].dtype == 'object':
            df[column] = le.fit_transform(df[column])

    # Llenar valores faltantes con la media (numéricos) o la moda (categóricos)
    for column in df.columns:
        if df[column].dtype in ['int64', 'float64']:
            df[column].fillna(df[column].mean(), inplace=True)
        else:
            df[column].fillna(df[column].mode()[0], inplace=True)
    return df

if __name__ == "__main__":
    show_project()