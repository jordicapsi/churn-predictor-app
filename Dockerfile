# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all necessary files into the container
COPY app/ app/
COPY model.pkl .
COPY scaler.pkl .
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit's default port
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
