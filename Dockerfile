# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables for Python
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory in the container
WORKDIR /data/app/

# Create a directory for Nginx configuration
RUN mkdir -p /etc/nginx

# Copy the Nginx configuration file into the container
COPY nginx/nginx.conf /etc/nginx/nginx.conf

# Copy the requirements file into the container at /data/app
COPY requirements.txt /data/app/

# Update the package lists and install development tools (including GCC)
RUN apt-get update && apt-get install -y build-essential

RUN python -m venv venv

# activate virtual environment
RUN . venv/bin/activate

# Upgrade pip and setuptools
RUN pip install --upgrade pip setuptools


# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /data/app
COPY . /data/app/

# Expose port 8000 for the Django application
EXPOSE 8000

# Run Gunicorn to serve the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
