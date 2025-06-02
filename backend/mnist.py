import streamlit as st
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import io

def load_and_preprocess_image(uploaded_file):
    # Read the image file
    image = Image.open(uploaded_file).convert('L')  # Convert to grayscale
    # Resize to 28x28 pixels
    image = image.resize((28, 28))
    # Convert to numpy array and normalize
    img_array = np.array(image)
    img_array = img_array / 255.0
    # Reshape for model input (1, 28, 28, 1)
    img_array = img_array.reshape(1, 28, 28, 1)
    return img_array

def create_model():
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        Flatten(),
        Dense(64, activation='relu'),
        Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam',
                 loss='sparse_categorical_crossentropy',
                 metrics=['accuracy'])
    return model

def train_model():
    # Load MNIST dataset
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    
    # Normalize and reshape data
    x_train = x_train.reshape((60000, 28, 28, 1)).astype('float32') / 255
    x_test = x_test.reshape((10000, 28, 28, 1)).astype('float32') / 255
    
    # Create and train model
    model = create_model()
    model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))
    
    # Save model
    model.save('mnist_model.h5')
    return model

def show_project():
    st.write("Upload an image of a handwritten number (0-9) to be predicted by a model trained on MNIST.")
    
    # Try to load the model, train if it doesn't exist
    try:
        model = load_model('mnist_model.h5')
    except:
        st.info("Training model for first use... This may take a few minutes.")
        model = train_model()
        st.success("Model training complete!")
    
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_container_width=True)
        
        # Preprocess the image and make prediction
        processed_image = load_and_preprocess_image(uploaded_file)
        prediction = model.predict(processed_image)
        predicted_digit = np.argmax(prediction[0])
        confidence = float(prediction[0][predicted_digit]) * 100
        
        # Display results
        st.success(f"Prediction: {predicted_digit}")
        st.write(f"Confidence: {confidence:.2f}%")
        
        # Display confidence bars for all digits
        st.write("### Confidence Distribution")
        for i, conf in enumerate(prediction[0]):
            st.progress(float(conf))
            st.write(f"Digit {i}: {float(conf)*100:.2f}%")

if __name__ == "__main__":
    show_project()