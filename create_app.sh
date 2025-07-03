#!/bin/bash

APP_NAME=$1
BACKEND_DIR="backend"
APPS_DIR="$BACKEND_DIR/apps"
SETTINGS_FILE="$BACKEND_DIR/easypark/settings.py"
VENV_ACTIVATE="$BACKEND_DIR/env/bin/activate"

if [ -z "$APP_NAME" ]; then
  echo "❌ Debes pasar el nombre de la app: ./create_app.sh nombre_app"
  exit 1
fi

# Crear carpeta apps si no existe
mkdir -p "$APPS_DIR"

# Activar entorno virtual
source "$VENV_ACTIVATE"

# Crear la app Django en la ruta correcta
mkdir -p "$APPS_DIR/$APP_NAME"
python "$BACKEND_DIR/manage.py" startapp "$APP_NAME" "$APPS_DIR/$APP_NAME"

echo "✅ App '$APP_NAME' creada en $APPS_DIR/$APP_NAME"

# Crear archivos base
touch "$APPS_DIR/$APP_NAME/serializers.py"
touch "$APPS_DIR/$APP_NAME/permissions.py"
echo -e "from django.urls import path\n\nurlpatterns = []" > "$APPS_DIR/$APP_NAME/urls.py"
echo "📄 Archivos serializers.py, permissions.py y urls.py creados."

# Añadir app a INSTALLED_APPS en settings.py
if grep -q "INSTALLED_APPS = \[" "$SETTINGS_FILE"; then
  # Verificar si ya está agregado
  if ! grep -q "apps.$APP_NAME" "$SETTINGS_FILE"; then
    sed -i "/INSTALLED_APPS = \[/a \ \ \ \ 'apps.$APP_NAME'," "$SETTINGS_FILE"
    echo "🧠 apps.$APP_NAME agregado a INSTALLED_APPS en $SETTINGS_FILE"
  else
    echo "ℹ️ apps.$APP_NAME ya estaba en INSTALLED_APPS"
  fi
else
  echo "⚠️ No se encontró INSTALLED_APPS en $SETTINGS_FILE. Agrégalo manualmente."
fi
