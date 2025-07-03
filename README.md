# 🚗 EasyParkingCL

**Encuentra, reserva y paga tu estacionamiento ideal usando IA, geolocalización y biometría.**  
EasyParkingCL es una plataforma inteligente (móvil y web) que conecta a conductores con los mejores lugares para estacionar según conveniencia, cercanía, tráfico en tiempo real y disponibilidad.

---

## 🌐 Visión General

> ¿Llegando al Portal Temuco o a un mall y no sabes dónde estacionar?  
> EasyParkingCL te guía al espacio más conveniente con ayuda de mapas, IA y sensores inteligentes.

---

## 📦 Estructura del Proyecto (Monorepo)

EasyParkingCL/
├── backend/ # API REST - Django + DRF
│ ├── apps/ # Apps modulares (parking, users, reservations, etc.)
│ ├── easypark/ # Configuración principal Django
│ ├── env/ # Entorno virtual (local)
│ ├── Dockerfile
│ ├── .env
│ └── README.md
├── frontend/ # App móvil - React Native (Expo)
│ ├── components/ # Componentes (Atomic Design)
│ ├── screens/ # Pantallas de la app
│ ├── assets/ # Íconos, imágenes
│ └── ...
├── scripts/ # Scripts útiles (crear apps, backups, etc.)
├── docs/ # Documentación técnica, flujos, mockups
├── .gitignore
├── .dockerignore
├── Makefile
└── README.md # Este archivo


---

## 🚀 Tecnologías

| Categoría          | Stack Tecnológico |
|--------------------|-------------------|
| **Frontend**       | React Native (Expo), React.js, TypeScript, Zustand, TailwindCSS, Three.js |
| **Backend**        | Python 3.8.7, Django REST Framework, PostgreSQL + PostGIS |
| **Autenticación**  | Firebase Auth, Google OAuth2, RUT/Correo, Huella, Voz, Rostro |
| **IA/ML**          | OpenAI, TensorFlow, Whisper, MediaPipe |
| **Pagos**          | Stripe / Transbank / MercadoPago |
| **Geolocalización**| Google Maps API, Mapbox |
| **DevOps**         | Docker, GitHub Actions, Terraform, NGINX |
| **Notificaciones** | Firebase Cloud Messaging |
| **Asíncronía**     | Celery + Redis |

---

## 🔐 Autenticación

- RUT + Contraseña
- Correo + Contraseña
- Google OAuth2
- Biometría:
  - 🧬 Rostro (MediaPipe)
  - 🖐️ Huella (lector móvil)
  - 🔊 Voz (Whisper)
- Verificación por código vía correo

---

## 🧠 Inteligencia Artificial

- 🔍 Recomendación automática del lugar ideal
- 🎙️ Asistente por voz
- 📊 Predicción de demanda
- 🤖 Reconocimiento biométrico seguro

---

## 🗺️ Funcionalidades principales

- Buscar estacionamientos por cercanía, precio o disponibilidad
- Reservar y pagar online
- Vista 3D (Three.js)
- Panel administrativo con métricas
- PWA + Dark mode + modo offline

---

## 🐳 Configuración rápida para desarrollo

### Requisitos previos

- Python 3.8.7
- Docker + Docker Compose
- Node.js y yarn/npm
- Firebase CLI

### Backend

```bash
cd backend
python3 -m venv env
source env/bin/activate
cp .env.example .env
make docker-up
make migrate-local
make createsuperuser-local
make run-local


🛠️ DevOps
CI/CD: GitHub Actions

Infraestructura como código: Terraform

NGINX + SSL para producción

Firebase para notificaciones push

📍 Roadmap
 Login con correo y Google

 Login por biometría

 Dashboard admin web

 Sensores físicos (IoT)

 IA predictiva de espacios

👤 Autor
Pedro Pablo Osorio San Martín
📫 posoriosanmartin@gmail.com
🔗 https://github.com/PPOSM1993

