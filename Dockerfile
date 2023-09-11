# Dockerfile to create a Docker image for the Streamlit app

# Creates a layer from the python:3.9 Docker image
FROM python:3.9

WORKDIR /app

# Copy all the files from the folders the Dockerfile is to the container root folder
COPY . .

# Install the modules specified in the pipfile
RUN pip install -r requirements.txt 

# The port on which a container listens for connections
EXPOSE 8501

# The command that run the app
CMD streamlit run main.py
