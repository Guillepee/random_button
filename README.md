# 🎲 Random Content Generator

![Banner](https://img.shields.io/badge/Random%20Content-Generator-6c5ce7?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.7+-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.2-009688?style=flat-square&logo=fastapi)
![Flet](https://img.shields.io/badge/Flet-0.20.0-ff69b4?style=flat-square)

A simple application that generates random quotes and jokes with just a button press. Built with a microservices architecture that separates the backend (REST API) from the frontend.

## ✨ Features

- 🔄 Random generation of quotes and jokes
- 🌐 REST API with FastAPI to serve content
- 🎨 Minimalist user interface built with Flet
- 🏗️ Object-oriented architecture with separation of concerns
- 🔍 Automatic API documentation with Swagger UI

## 🚀 Getting Started

### Prerequisites

- Docker
- Docker Compose (optional)

### Installation and Running with Docker

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/random_button.git
   cd random_button
   ```

2. Build the Docker image:
   ```bash
   docker buildx build -t random-button-app:latest .
   ```

3. Run the container:
   ```bash
   docker run -p 8080:8080 -p 8000:8000 --rm --name random-button-app random-button-app:latest
   ```

The application will be available at:
- Frontend: `http://localhost:8080`
- Backend API: `http://localhost:8000`

## 🏗️ Project Structure

```
random_button/
├── backend/                # REST API Server
│   ├── backend_app.py      # Backend entry point
│   └── database_repository.py # SQLite database repository
├── frontend/              # Client Application
│   └── frontend_app.py    # Flet Application
├── Dockerfile            # Docker configuration
├── requirements.txt      # Project dependencies
├── .env                 # Environment variables (not versioned)
└── README.md            # This file
```

## 🖥️ Usage

Once the Docker container is running, you can access:

- **Frontend Application**: `http://localhost:8080`
- **Backend API**: `http://localhost:8000`
- **API Documentation**: `http://localhost:8000/docs`

## 📡 API Endpoints

### Get Random Content

```
GET /random/{type}
```

Where `{type}` can be:
- `joke`: Returns a random joke
- `quote`: Returns a random inspirational quote

**Example Response**:

```json
{
  "type": "joke",
  "content": "What is the computer's favorite snack to eat?... Microchips!"
}
```

## 🧩 Architecture

The project follows a microservices architecture with:

### Backend

- **FastAPI**: Modern API framework
- **SQLite**: Lightweight database for storage
- **Docker**: Application containerization
- **Repository Pattern**: For data access

### Frontend

- **Flet**: UI Framework with Flutter/Python
- **Dark Theme**: Modern interface
- **Scrollable Containers**: For content display
- **Chuck Norris API Integration**: For additional jokes

## 📦 Dependencies

- **FastAPI**: Modern API framework
- **SQLite**: Lightweight database for storage
- **Docker**: Application containerization
- **Flet**: UI Framework with Flutter/Python
- **Chuck Norris API**: For additional jokes

## 🐳 Docker Build Details

The project uses a multi-stage Docker build to optimize the image size:

### Stage 1: Builder
- Uses `python:3.11-slim-buster` as base image
- Installs build dependencies
- Creates and configures a Python virtual environment
- Installs all project dependencies in the virtual environment

### Stage 2: Final Image
- Uses `python:3.11-slim-buster` as base image
- Copies only the virtual environment from the builder stage
- Contains only runtime dependencies
- Results in a significantly smaller image size

This approach reduces the final image size by:
- Excluding build tools and dependencies
- Including only necessary runtime files
- Using a virtual environment for Python packages
- Removing temporary files and caches

The final image is optimized for production use while maintaining all functionality.

