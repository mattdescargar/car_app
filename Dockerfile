# FROM python:3.12.3
# ENV DEPLOYMENTDIR /code
# COPY / $DEPLOYMENTDIR
# WORKDIR $DEPLOYMENTDIR
# RUN mkdir storage \
#     & pip3 install -r requirements.txt
# Use Python 3.12.3 as the base image
FROM python:3.12.3

# Set the working directory in the container

WORKDIR /app

# Copy the current directory contents into the container at /code
COPY requirements.txt requirements.txt

# Create a directory for storing Django static and media files
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8080"]