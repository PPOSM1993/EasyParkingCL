#!/bin/bash
set -e

echo "⏳ Esperando a que la base de datos esté lista..."

until pg_isready -h "$POSTGRES_HOST" -p "$POSTGRES_PORT" -U "$POSTGRES_USER"; do
  echo "Esperando a que la base de datos responda..."
  sleep 2
done

echo "🛠️ Ejecutando migraciones..."
python manage.py migrate

echo "⚙️ Recolectando archivos estáticos..."
python manage.py collectstatic --noinput

echo "🚀 Iniciando servidor Django..."
gunicorn easypark.wsgi:application --bind 0.0.0.0:8000
