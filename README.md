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

- Python 3.7+
- pip (gestor de paquetes de Python)

### Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/random_button.git
   cd random_button
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requeriments
   ```

## 🏗️ Estructura del proyecto

```
random_button/
├── backend/                # Servidor API REST
│   ├── data/               # Datos de frases y chistes
│   │   └── content_data.json
│   ├── backend_app.py      # Punto de entrada del backend
│   ├── class_repository.py # Repositorio de datos
│   ├── config.py           # Configuración del backend
│   └── README.md           # Documentación específica del backend
├── frontend/               # Aplicación cliente
│   ├── frontend_app.py     # Aplicación Flet
│   ├── example.js          # Ejemplo de cliente JavaScript
│   └── index.html          # Ejemplo de cliente HTML
├── venv/                   # Entorno virtual (ignorado en git)
├── requeriments            # Dependencias del proyecto
└── README.md               # Este archivo
```

## 🖥️ Uso

### Ejecutando el backend

1. Navega al directorio del backend:
   ```bash
   cd backend
   ```

2. Inicia el servidor:
   ```bash
   python backend_app.py
   ```

3. El servidor estará disponible en `http://localhost:8000`

### Ejecutando el frontend

#### Aplicación Flet

1. Navega al directorio del frontend:
   ```bash
   cd frontend
   ```

2. Inicia la aplicación:
   ```bash
   python frontend_app.py
   ```

3. La aplicación se abrirá automáticamente en tu navegador predeterminado

#### Cliente web alternativo

También puedes usar el cliente web HTML/JS incluido:

1. Abre el archivo `frontend/index.html` en tu navegador web
2. Asegúrate de que el backend esté en ejecución
3. Haz clic en el botón para obtener contenido aleatorio

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
  "content": "Why don't scientists trust atoms? Because they make up everything!",
  "id": 42,
  "author": "Anonymous"
}
```

### Documentación de la API

Una vez que el servidor esté en ejecución, puedes acceder a la documentación interactiva de la API en:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🧩 Arquitectura

El proyecto sigue una arquitectura de microservicios con separación clara entre el backend y el frontend:

### Backend

- **FastAPI**: Framework moderno y de alto rendimiento para construir APIs con Python
- **Patrón Repositorio**: Abstracción para el acceso a datos
- **Enumeraciones**: Uso de Enum para tipos de contenido (chistes/frases)

### Frontend

- **Flet**: Framework para construir interfaces de usuario con Flutter y Python
- **Tema oscuro**: Interfaz moderna con modo oscuro
- **Contenedores desplazables**: Para mostrar múltiples elementos de contenido


