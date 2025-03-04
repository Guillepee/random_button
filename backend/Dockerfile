# Use the base image
FROM random-button-base:latest

# Copy backend files
COPY . .

# Create directory for database
RUN mkdir -p /data

# Set environment variables
ENV DB_PATH=/data/repository.db
ENV HOST=0.0.0.0
ENV PORT=8000
ENV DEBUG=False
ENV ALLOWED_ORIGINS=http://localhost:8080,http://localhost:8550

# Expose port
EXPOSE 8000

# Run the application
CMD ["python", "backend_app.py"] 