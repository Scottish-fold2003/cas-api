#Dockerfile
FROM python:3.13.5-slim AS builder

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.13.5-slim

# Set the working directory in the container
WORKDIR /app
RUN apt-get -y update; apt-get -y install curl
RUN apt-get install -y iputils-ping
RUN apt-get install tzdata -y
ENV TZ="Asia/Bangkok"

# Copy the installed dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# COPY hosts-file /etc/hosts

WORKDIR /app

COPY ./src/ .

# RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

EXPOSE 8000

CMD ["fastapi", "run", "main.py", "--port", "8000"]