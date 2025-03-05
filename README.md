# 🎲 Random Content Generator

![Banner](https://img.shields.io/badge/Random%20Content-Generator-6c5ce7?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.7+-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.2-009688?style=flat-square&logo=fastapi)
![Flet](https://img.shields.io/badge/Flet-0.20.0-ff69b4?style=flat-square)

Una aplicación sencilla y directa que genera citas y chistes aleatorios con solo pulsar un botón. Construida con una arquitectura de microservicios que separa el backend (API REST) del frontend.

## ✨ Características

- 🔄 Generación aleatoria de citas y chistes 
- 🌐 API REST con FastAPI para servir el contenido
- 🎨 Interfaz de usuario minimalista construida con Flet
- 🏗️ Arquitectura orientada a objetos con separación de responsabilidades
- 🔍 Documentación automática de la API con Swagger UI

## 🚀 Comenzando

### Requisitos previos

- Docker

### Instalación y Ejecución con Docker

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/random_button.git
   cd random_button
   ```

2. Construye la imagen de Docker:
   ```bash
   docker buildx build -t random-button-app:latest .
   ```

3. Ejecuta el contenedor:
   ```bash
   docker run -p 8080:8080 -p 8000:8000 --rm --name random-button-app random-button-app:latest
   ```

La aplicación estará disponible en:
- Frontend: `http://localhost:8080`
- Backend API: `http://localhost:8000`

## 🏗️ Estructura del proyecto

```
random_button/
├── backend/                # Servidor API REST
│   ├── backend_app.py      # Punto de entrada del backend
│   └── database_repository.py # Repositorio de base de datos SQLite
├── frontend/              # Aplicación cliente
│   └── frontend_app.py    # Aplicación Flet
├── Dockerfile            # Configuración de Docker
├── requirements.txt      # Dependencias del proyecto
├── .env                 # Variables de entorno (no versionado)
└── README.md            # Este archivo
```

## 🖥️ Uso

Una vez que el contenedor Docker esté en ejecución, puedes acceder a:

- **Aplicación Frontend**: `http://localhost:8080`
- **API Backend**: `http://localhost:8000`
- **Documentación API**: `http://localhost:8000/docs`

## 📡 API Endpoints

### Obtener contenido aleatorio

```
GET /random/{type}
```

Donde `{type}` puede ser:
- `joke`: Devuelve un chiste aleatorio
- `quote`: Devuelve una frase inspiradora aleatoria

**Ejemplo de respuesta**:

```json
{
{
  "type": "joke",
  "content": "What is the computer's favorite snack to eat?... Microchips!"
}
}
```

## 🧩 Arquitectura

El proyecto sigue una arquitectura de microservicios con:

### Backend

- **FastAPI**: Framework moderno para APIs
- **SQLite**: Base de datos ligera para almacenamiento
- **Docker**: Containerización de la aplicación
- **Patrón Repositorio**: Para acceso a datos

### Frontend

- **Flet**: Framework para UI con Flutter/Python
- **Tema oscuro**: Interfaz moderna
- **Contenedores desplazables**: Para mostrar contenido
- **Integración con Chuck Norris API**: Para obtener chistes adicionales


## 📦 Dependencias

- **FastAPI**: Framework moderno para APIs
- **SQLite**: Base de datos ligera para almacenamiento
- **Docker**: Containerización de la aplicación
- **Flet**: Framework para UI con Flutter/Python
- **Chuck Norris API**: Para obtener chistes adicionales

