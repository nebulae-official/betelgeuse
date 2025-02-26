FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy the required files into the container
COPY . /app/

# Install system dependencies
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir -r dev-requirements.txt

# Install uv (using the install script from Astral's documentation)
RUN curl -sSfL https://uv.astral.sh/install.sh | sh

# Run tests
RUN python -m pytest

# Run the hello.py application by default
CMD ["python", "hello.py"]
