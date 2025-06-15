# Use official Python base image
FROM python:3.10

# Set working directory inside container
WORKDIR /app

# Copy all files into the container
COPY . .

# Install required packages
RUN pip install --no-cache-dir fastapi uvicorn redis

# Expose the port FastAPI runs on
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
