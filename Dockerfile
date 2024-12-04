FROM python:3.9.20

RUN apt-get update

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the source code
WORKDIR /app
COPY . .
RUN mkdir -p /app/static/storage