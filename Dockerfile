# Stage 1: Builder
FROM python:3.11-slim-buster as builder

WORKDIR /app

# Instalar solo las dependencias necesarias para compilar
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

# Copiar requirements y crear entorno virtual
COPY requirements.txt .
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Instalar dependencias en el entorno virtual
RUN pip install --no-cache-dir -r requirements.txt && \
    rm -rf ~/.cache/pip/*

# Stage 2: Final
FROM python:3.11-slim-buster

# Copiar el entorno virtual del builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Configurar variables de entorno
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

WORKDIR /app

# Copiar todo el código
COPY . .

# Exponer puertos
EXPOSE 8000 8080

# Comando de inicio
CMD ["sh", "-c", "python backend/backend_app.py & python frontend/frontend_app.py"]
