# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the files from the current directory to the working directory
COPY . .

# Expose the port on which the Flask app will run (default is 5000)
EXPOSE 5000


# Run the Flask app when the container launches
CMD ["python","app.py"]
