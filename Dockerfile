FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DB_PATH=/app/repository.db \ 
    HOST=0.0.0.0 \
    BACKEND_PORT=8000 \
    FRONTEND_PORT=8080 \
    DEBUG=False \
    ALLOWED_ORIGINS=http://localhost:8080,http://localhost:8550 \
    BACKEND_URL=http://localhost:8000 \
    CHUCK_NORRIS_API_URL=https://api.chucknorris.io/jokes/random


# Expose necessary ports
EXPOSE 8000 8080

# Start both backend and frontend services
CMD ["sh", "-c", "python backend/backend_app.py & python frontend/frontend_app.py"]
