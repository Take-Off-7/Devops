# Use a recent lightweight Python image
FROM python:3.12-slim

# Set environment variable for app directory
ENV APP_HOME=/app

# Set working directory
WORKDIR $APP_HOME

# Copy and install dependencies first for caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Default command to run your app
ENTRYPOINT ["python"]
CMD ["app.py"]
