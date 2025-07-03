SHELL := /bin/bash

# ========================
# 🧠 VARIABLES
# ========================
MANAGE=python manage.py
DJANGO_DIR=backend
VENV_ACTIVATE=source env/bin/activate

# ========================
# ⚙️  LOCAL ENV (VENV)
# ========================

run-local:
	cd $(DJANGO_DIR) && $(VENV_ACTIVATE) && $(MANAGE) runserver

migrate-local:
	cd $(DJANGO_DIR) && $(VENV_ACTIVATE) && $(MANAGE) migrate

makemigrations-local:
	cd $(DJANGO_DIR) && $(VENV_ACTIVATE) && $(MANAGE) makemigrations

createsuperuser-local:
	cd $(DJANGO_DIR) && $(VENV_ACTIVATE) && $(MANAGE) createsuperuser

init-local:
	cd $(DJANGO_DIR) && $(VENV_ACTIVATE) && $(MANAGE) makemigrations && $(MANAGE) migrate && $(MANAGE) createsuperuser

shell-local:
	cd $(DJANGO_DIR) && $(VENV_ACTIVATE) && $(MANAGE) shell

test-local:
	cd $(DJANGO_DIR) && $(VENV_ACTIVATE) && $(MANAGE) test

create-app:
	@if [ -z "$(name)" ]; then \
		echo "❌ Debes proporcionar un nombre: make create-app name=mi_app"; \
	else \
		mkdir -p backend/apps/$(name) && \
		source backend/env/bin/activate && \
		python backend/manage.py startapp $(name) backend/apps/$(name); \
		echo "✅ App '$(name)' creada en backend/apps/$(name)"; \
		touch backend/apps/$(name)/serializers.py && \
		touch backend/apps/$(name)/permissions.py && \
		echo "from django.urls import path\n\nurlpatterns = []" > backend/apps/$(name)/urls.py; \
		if grep -q "INSTALLED_APPS = \[" backend/easypark/settings.py; then \
			sed -i "/INSTALLED_APPS = \[/a \ \ \ \ 'apps.$(name)'," backend/easypark/settings.py; \
			echo "🧠 apps.$(name) agregado a INSTALLED_APPS en backend/easypark/settings.py"; \
		else \
			echo "⚠️ No se encontró INSTALLED_APPS en backend/easypark/settings.py. Agrégalo manualmente."; \
		fi; \
	fi


# ========================
# 🐳 DOCKER COMMANDS
# ========================

docker-up:
	docker-compose up --build

docker-down:
	docker-compose down

docker-web:
	docker-compose run web bash

docker-migrate:
	docker-compose run web python manage.py migrate

docker-makemigrations:
	docker-compose run web python manage.py makemigrations
	

docker-createsuperuser:
	docker-compose run web python manage.py createsuperuser

init-docker:
	docker-compose run web python manage.py makemigrations
	docker-compose run web python manage.py migrate
	docker-compose run web python manage.py createsuperuser

docker-test:
	docker-compose run web python manage.py test

# ========================
# 🧼 UTILITY
# ========================

clean-pycache:
	find . -type d -name '__pycache__' -exec rm -r {} +
	find . -type f -name '*.pyc' -delete

rebuild:
	docker-compose down -v
	docker-compose up --build



#make run-local               # Corre en entorno virtual
#make migrate-local
#make createsuperuser-local

#make docker-up               # Levanta Docker
#make docker-migrate
#make docker-createsuperuser
#make docker-test

#make clean-pycache           # Limpia basura de Python
#make rebuild                 # Apaga y reconstruye todo


#make create-app name=accounts           # Crea la app dentro de backend/apps/accounts
#make makemigrations-local
#make docker-makemigrations
#make init-local                         # makemigrations + migrate + createsuperuser
#make init-docker