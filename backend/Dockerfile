# backend/Dockerfile

FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Instalar dependencias del SO necesarias para GDAL y PostgreSQL
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    gdal-bin \
    libgdal-dev \
    libpq-dev \
    postgresql-client \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copiar y instalar dependencias de Python
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copiar el código fuente
COPY . .

# Configurar variable de entorno para GDAL (ajusta la ruta si es necesario)
ENV GDAL_LIBRARY_PATH=/usr/lib/libgdal.so

EXPOSE 8000
