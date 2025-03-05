#!/bin/bash

# Iniciar el backend con auto-recarga
nodemon --watch backend -e py --exec "python backend/backend_app.py" &

# Iniciar el frontend con auto-recarga
nodemon --watch frontend -e py --exec "python frontend/frontend_app.py" &

# Mantener el contenedor en ejecución
tail -f /dev/null 