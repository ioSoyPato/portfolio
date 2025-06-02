# Predict the breed of a dog

import streamlit as st
from PIL import Image

def show_project():
    # Project Header with custom styling
    st.markdown("""
        <div class="project-card">
            <h1>Dog Breed Prediction</h1>
            <p>Upload a photo of a dog and let our AI model predict its breed!</p>
            <div class="skill-tag">Computer Vision</div>
            <div class="skill-tag">Deep Learning</div>
            <div class="skill-tag">Image Processing</div>
        </div>
    """, unsafe_allow_html=True)
    
    # File upload section with styled container
    st.markdown("""
        <div class="project-card">
            <h2>Upload Image</h2>
            <div class="uploadedFile">
                <p>Drag and drop your dog's photo here</p>
                <p class="file-hint">(Supported formats: JPG, JPEG, PNG)</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])  # Label hidden as it's shown in HTML

    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)
            
            # Display uploaded image with styling
            st.markdown("""
                <div class="project-card">
                    <h2>Uploaded Image</h2>
                </div>
            """, unsafe_allow_html=True)
            st.image(image, caption="Your Dog", use_column_width=True)

            # Prediction section
            col1, col2, col3 = st.columns([1,2,1])
            with col2:
                if st.button("Predict Breed", use_container_width=True):
                    # Add a loading spinner while processing
                    with st.spinner('Analyzing image...'):
                        # Here you would add your actual prediction logic
                        # For now, we'll just show a placeholder result
                        st.markdown("""
                            <div class="success">
                                <h3>Prediction Results</h3>
                                <p>Predicted Breed: Golden Retriever</p>
                                <p>Confidence: 95%</p>
                            </div>
                        """, unsafe_allow_html=True)
        except Exception as e:
            st.markdown(f"""
                <div class="error">
                    <h3>Error</h3>
                    <p>Error processing the image: {str(e)}</p>
                    <p>Please ensure you've uploaded a valid image file.</p>
                </div>
            """, unsafe_allow_html=True)

    # Add custom CSS
    st.markdown("""
        <style>
        .file-hint {
            color: #666;
            font-size: 0.9em;
            margin-top: 0.5rem;
        }
        
        .uploadedFile {
            margin: 2rem 0;
            padding: 2rem;
            background-color: #f8f9fa;
            border: 2px dashed #ccc;
            border-radius: 8px;
            text-align: center;
            transition: border-color 0.3s ease;
        }
        
        .uploadedFile:hover {
            border-color: #2E4057;
        }
        
        .stButton button {
            background-color: #2E4057;
            color: white;
            padding: 0.75rem 1.5rem;
            border-radius: 20px;
            border: none;
            transition: background-color 0.3s ease;
        }
        
        .stButton button:hover {
            background-color: #1a2633;
        }
        </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    show_project()
    