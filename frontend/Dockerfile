# Use the base image
FROM random-button-base:latest

# Copy frontend files
COPY . .

# Set environment variables
ENV PORT=8550
ENV BACKEND_URL=http://backend:8000
ENV CHUCK_NORRIS_API_URL=https://api.chucknorris.io/jokes/random

# Expose port
EXPOSE 8550

# Run the application
CMD ["python", "frontend_app.py"] 