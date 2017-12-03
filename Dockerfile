############################################################
# Dockerfile to build Python WSGI Application Containers   #
# Based on Ubuntu										   #
############################################################

# Set the base image to Ubuntu
FROM ubuntu:latest

# File Author / Maintainer
MAINTAINER GabrielGrimberg
Label org.label-schema.group="monitoring"

# Update the sources list
RUN apt-get update

# Install Python and Basic Python Tools
RUN apt-get install -y python3 python3-pip mysql-client libmysqlclient-dev

#copy container-server.py into /application folder
ADD . /my_application

# Copy the application folder inside the container
# COPY /templates /application

# Upgrade  PIP
RUN pip3 install --upgrade pip

# Get pip to download and install requirements:
RUN pip3 install -r /my_application/requirements.txt

# Expose ports
EXPOSE 5000 8000
# EXPOSE 8000

# Set the default directory where CMD will execute
WORKDIR /my_application

# Set the default command to execute
# when creating a new container
# i.e. using Flask to serve the application
CMD python3 container-server.py