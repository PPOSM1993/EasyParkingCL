

---

## 📁 2. `backend/README.md`

```markdown
# 🧠 EasyParkingCL – Backend

Backend desarrollado en Django + Django REST Framework para gestionar usuarios, estacionamientos, reservas y más.

---

## 📁 Estructura

## 🧪 Desarrollo local con entorno virtual

```bash
cd backend
python3.8 -m venv env
source env/bin/activate
pip install -r requirements.txt


---

## ⚙️ Tecnologías Backend

- Django 4+
- Django REST Framework
- PostgreSQL + PostGIS
- Redis + Celery
- Firebase Admin SDK
- Autenticación avanzada (Google, correo, biometría)
- Geolocalización
- Docker + Compose

---

## 📦 Apps Modulares

- `users`: usuarios, perfiles, RUT, biometría
- `parking`: zonas, espacios, sensores
- `reservations`: gestión de reservas y pagos
- `payments`: Stripe, Transbank, MercadoPago
- `notifications`: Firebase Cloud Messaging
- `ai`: motores de predicción y recomendación

---

## ⚙️ Comandos útiles (Makefile)

```bash
make run-local              # Levantar servidor local
make migrate-local          # Aplicar migraciones
make createsuperuser-local  # Crear usuario admin
make create-app name=foo    # Crear nueva app
make docker-up              # Levantar todo con Docker
make docker-down            # Detener servicios


DEBUG=True
SECRET_KEY=your-secret-key
POSTGRES_DB=easyparking
POSTGRES_USER=postgres
POSTGRES_PASSWORD=secret
EMAIL_HOST_USER=youremail@example.com
EMAIL_HOST_PASSWORD=yourpassword
FIREBASE_API_KEY=...


🚦 API REST
Autenticación con JWT

Endpoints protegidos por permisos por rol

URLs versionadas (/api/v1/)

👨‍💻 Autor
Pedro Pablo Osorio San Martín
📫 pedro@example.com

make test-local         # Test en entorno virtual
make docker-test        # Test vía Docker
