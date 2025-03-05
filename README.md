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

## 🐳 Docker Image Structure

The project uses a system of three images:
- **Base image**: Contains all common dependencies
- **Development image**: For development environment with additional tools
- **Production image**: Size-optimized for deployment

## 🚀 Getting Started

### Prerequisites

- Docker
- VSCode (recommended, with Remote Containers extension)


### Development Options

#### Option 1: Using VSCode

1. Open the project in VSCode
2. When the "Reopen in Container" notification appears, click on it
   (or press F1 and select "Remote-Containers: Reopen in Container")
3. Done! VSCode will open the project inside the development container

**Development environment features:**
- Auto-reload when code changes
- Development tools installed (pytest, black, flake8, pylint)
- Integrated debugging with VSCode
- DEBUG mode enabled for detailed messages

### Installation and Running with Docker

1. Build the Docker image:
   ```bash
   docker buildx build --platform linux/amd64 -t guillepee/button-project:latest -f Dockerfile.prod .
   ```
2. Run the application
docker run -d -p 8080:8080 -p 8000:8000 --name button-app guillepee/button-project:latest


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
├── Dockerfile.base        # Base image configuration
├── Dockerfile.dev         # Development container configuration
├── Dockerfile.prod        # Production container configuration
├── .devcontainer/         # VSCode container configuration
├── requirements.txt       # Project dependencies
├── .env                   # Environment variables (not versioned)
└── README.md              # This file
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

## 🐳 Docker Configuration Files

The project includes several Docker-related files:

- `Dockerfile.base`: Base image with all common dependencies
- `Dockerfile.dev`: Development environment with additional tools and auto-reload
- `Dockerfile.prod`: Optimized image for production
- `.devcontainer/devcontainer.json`: Container configuration for VSCode
- `.devcontainer/dev-entrypoint.sh`: Script to start the application in development mode

## 📦 Dependencies

- **FastAPI**: Modern API framework
- **SQLite**: Lightweight database for storage
- **Docker**: Application containerization
- **Flet**: UI Framework with Flutter/Python
- **Chuck Norris API**: For additional jokes

