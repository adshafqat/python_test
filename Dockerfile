FROM quay.io/devfile/python:slim

# By default, listen on port 8081
EXPOSE 8081/tcp
ENV FLASK_PORT=8081

# Set the working directory in the container
WORKDIR /projects

# Install any dependencies
RUN pip install flask
RUN pip install pyjwt
RUN pip install requests
RUN pip install cryptography
# Copy the content of the local src directory to the working directory
COPY . .

# Specify the command to run on container start
CMD [ "python", "./app.py" ]
