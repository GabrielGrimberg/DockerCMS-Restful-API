############################################################
# Dockerfile to build Python WSGI Application Containers
# Based on Ubuntu
############################################################
# Set the base image to Ubuntu
FROM ubuntu:latest
MAINTAINER GabrielGrimberg
Label org.label-schema.group="monitoring"

# Update the sources list
RUN apt-get update

# Install Python and Basic Python Tools
RUN apt-get install -y python3 python3-pip

# Copy container-server.py into /app folder 
ADD /my_application /my_application

# Upgrade  PIP
RUN pip3 install --upgrade pip

# Get pip to download and install requirements:
RUN pip3 install -r /my_application/requirements.txt

# Install curl and docker
RUN apt-get install -y curl
RUN curl -fsSL get.docker.com|sh

# Expose ports
EXPOSE 8080

# Set the default directory where CMD will execute
WORKDIR /my_application

# Set the default command to execute
# when creating a new container
# i.e. using Flask to serve the application
CMD python3 container-server.py