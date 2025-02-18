FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    portaudio19-dev \
    python3-pyaudio \
    alsa-utils \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Create non-root user for security
RUN useradd -m appuser && \
    chown -R appuser:appuser /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application
COPY . .

# Create and set permissions for archive directory
RUN mkdir -p /app/archive && \
    chown -R appuser:appuser /app/archive && \
    chmod 777 /app/archive

# Create Python package structure
RUN mkdir -p /app/src/packages/tts && \
    touch /app/src/packages/__init__.py && \
    touch /app/src/packages/tts/__init__.py

# Switch to non-root user
USER appuser

# Environment setup
ENV PYTHONPATH=/app
ENV ARCHIVE_PATH=/app/archive
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV NAME Linguist

# Run main.py when the container launches
CMD ["python", "main.py"]