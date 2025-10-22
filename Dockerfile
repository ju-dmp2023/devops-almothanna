# -----------------------------------------------
# Dockerfile for Calculator Application
# -----------------------------------------------

# Use the official Python 3.12 slim image (small and clean)
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements file first to leverage Docker layer caching
COPY requirements.txt .

# Upgrade pip and install Python dependencies listed in requirements.txt
RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy all remaining files from the BE folder to the container
COPY . .

# Expose default REST API port (optional if app uses FastAPI)
EXPOSE 5000

# Define the default command to run the calculator app
# This allows passing CLI arguments like: docker run image --add 1 2
ENTRYPOINT ["python", "calculator.py"]

# -----------------------------------------------
# Example usage:
# Build: docker build -t mothana-calculator .
# Run:   docker run --rm mothana-calculator --add 2 3
# -----------------------------------------------
