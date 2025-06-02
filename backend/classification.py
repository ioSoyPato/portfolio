import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

def show_project():
    # Add custom CSS class to title
    st.markdown("<h1>Classification Model</h1>", unsafe_allow_html=True)
    st.markdown("""
        <div class='project-card'>
            Este proyecto realiza una clasificación a partir de un dataset cargado por el usuario.
            Sigue los pasos a continuación para analizar tus datos.
        </div>
    """, unsafe_allow_html=True)
    
    # File upload with styled container
    st.markdown("<h2>Carga de Datos</h2>", unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="uploadedFile">', unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Sube tu archivo CSV", type=["csv"])
        st.markdown('</div>', unsafe_allow_html=True)
    
    target_column = st.text_input("Nombre de la columna objetivo (target):")
    
    if uploaded_file is not None and target_column:
        try:
            # Dataset display
            df = pd.read_csv(uploaded_file)
            st.markdown("<div class='success'>Dataset cargado con éxito!</div>", unsafe_allow_html=True)
            st.dataframe(df.head())

            # Preprocessing section
            st.markdown("<h2>Preprocesamiento de Datos</h2>", unsafe_allow_html=True)
            df = preprocess_data(df, target_column)
            st.markdown("<div class='project-card'>", unsafe_allow_html=True)
            st.write("Vista previa de datos procesados:")
            st.dataframe(df.head())
            st.markdown("</div>", unsafe_allow_html=True)

            # Split data and train model
            X = df.drop(target_column, axis=1)
            y = df[target_column]
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Train model
            st.markdown("<h2>Entrenamiento del Modelo</h2>", unsafe_allow_html=True)
            with st.spinner('Entrenando el modelo...'):
                model = RandomForestClassifier(random_state=42)
                model.fit(X_train, y_train)
                predictions = model.predict(X_test)
                accuracy = accuracy_score(y_test, predictions)

            # Metrics display with styled cards
            st.markdown("<h2>Rendimiento del Modelo</h2>", unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"""
                    <div class='project-card'>
                        <h3>Precisión (Accuracy)</h3>
                        <h2>{accuracy:.2f}</h2>
                    </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("""
                    <div class='project-card'>
                        <h3>Reporte de Clasificación</h3>
                """, unsafe_allow_html=True)
                st.text(classification_report(y_test, predictions))
                st.markdown("</div>", unsafe_allow_html=True)

            # Predictions section
            st.markdown("<h2>Realizar Predicciones</h2>", unsafe_allow_html=True)
            st.markdown('<div class="uploadedFile">', unsafe_allow_html=True)
            uploaded_new_data = st.file_uploader("Sube un CSV con los nuevos datos (sin columna target)", type=["csv"], key="new_data")
            st.markdown('</div>', unsafe_allow_html=True)

            if uploaded_new_data is not None:
                try:
                    new_data = pd.read_csv(uploaded_new_data)
                    st.markdown("<div class='success'>Nuevos datos cargados con éxito!</div>", unsafe_allow_html=True)
                    st.dataframe(new_data)
                    new_data = preprocess_data(new_data, target_column)
                    predictions = model.predict(new_data)
                    st.markdown("<div class='project-card'>", unsafe_allow_html=True)
                    st.write("Predicciones:")
                    result_df = pd.DataFrame({'Predicción': predictions})
                    st.dataframe(result_df)
                    st.markdown("</div>", unsafe_allow_html=True)
                except Exception as e:
                    st.markdown(f"<div class='error'>Error al procesar nuevos datos: {str(e)}</div>", unsafe_allow_html=True)
        except Exception as e:
            st.markdown(f"<div class='error'>Error al procesar datos: {str(e)}</div>", unsafe_allow_html=True)

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