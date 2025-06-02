FROM python:3.9-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Replace tensorflow-macos with regular tensorflow for Linux compatibility
RUN grep -v "tensorflow-macos" requirements.txt > requirements_linux.txt && \
    echo "tensorflow>=2.15.0" >> requirements_linux.txt && \
    pip install -r requirements_linux.txt && \
    pip install anthropic

# Copy the rest of the application
COPY . .

# Expose the port Streamlit runs on
EXPOSE 8501

# Command to run the application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
