# Use official lightweight Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies (if you have requirements.txt)
RUN pip install -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "web.py"]
