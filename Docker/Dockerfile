# This is the basic image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the file(s) into the container at /app
COPY ./server.py /app

# Install any needed packages specified in requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for the server
EXPOSE 8888

# Run server.py when the container launches
CMD ["python", "server.py"]