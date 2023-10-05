# Use the official Python image as the base image
FROM python:3.11.3-slim-bullseye

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y gcc default-libmysqlclient-dev pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install any necessary dependencies
RUN pip install -r requirements.txt

# Expose the port your Flask app will run on (adjust as needed)
EXPOSE 9999

# Define the command to run your Flask app
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=9999"]
