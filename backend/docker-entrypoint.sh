#!/bin/bash

echo "🛠️ Ejecutando migraciones..."
python manage.py migrate

echo "⚙️ Recolectando archivos estáticos..."
python manage.py collectstatic --noinput

echo "🚀 Iniciando servidor Django..."
gunicorn easypark.wsgi:application --bind 0.0.0.0:8000
