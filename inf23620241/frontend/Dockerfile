FROM python:3.9-slim-buster

# Set environment variables, recommended to udpate the mysql password and use  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory files (on your machine) to the container
ADD . /app/

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 8080

# Start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]