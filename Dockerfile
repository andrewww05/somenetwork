# Stage 1: Build stage
FROM python:3-alpine AS builder

WORKDIR /app

# Install PostgreSQL development packages
RUN apk add --no-cache build-base postgresql-dev

# Create a virtual environment
RUN python3 -m venv venv
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Stage 2: Final stage
FROM python:3-alpine AS runner

WORKDIR /app

# Copy virtual environment and application files
COPY --from=builder /app/venv venv
COPY . .

# Set environment variables
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV FLASK_APP=app/app.py

# Expose port
EXPOSE 8080

# Start the application
CMD ["gunicorn", "--bind", ":8080", "--workers", "2", "app:app"]
