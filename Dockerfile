# Use an official Python base image
FROM python:3.10-slim

# Set a working directory inside the container
WORKDIR /app

# Copy the project files to the container
COPY . /app

# Install necessary tools to build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install project dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose the port where the application will run
EXPOSE 8000

# Default command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
