#!/bin/bash

echo "🟢 Activando entorno virtual..."
cd backend || exit
source env/bin/activate
echo "🚀 Levantando servidor Django localmente..."
python manage.py runserver
