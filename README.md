# EasyParkingCL

# 🚗 Parking App – Encuentra y Reserva tu Estacionamiento Inteligente

Plataforma inteligente (web y móvil) que permite a los usuarios encontrar, reservar y pagar estacionamientos disponibles usando inteligencia artificial, geolocalización, biometría y más.

---

## 📦 Estructura del Proyecto (Monorepo)


---

## 🚀 Tecnologías

- **Frontend Web**: React, TypeScript, Zustand, TailwindCSS / Material UI
- **Mobile**: React Native (Expo), Zustand
- **Backend**: Python 3.8.7, Django REST Framework, PostgreSQL, Redis, Celery
- **Autenticación**: Firebase Auth, Google OAuth2, biometría (voz, rostro, huella)
- **IA**: Recomendaciones inteligentes, reconocimiento de voz y rostro (OpenAI, TensorFlow, Whisper, MediaPipe)
- **Pagos**: Stripe / MercadoPago / Transbank
- **DevOps**: Docker, GitHub Actions, Terraform, NGINX, Firebase Cloud Messaging

---

## 🔐 Autenticación

- Usuario/Contraseña
- Login con Google
- Reconocimiento biométrico:
  - Huella
  - Voz
  - Rostro

---

## 🧠 Inteligencia Artificial

- Recomendación de estacionamientos personalizados
- Asistente de voz para buscar y reservar
- Reconocimiento de voz, rostro y huella para autenticación
- Predicción de disponibilidad de estacionamientos

---

## 🗺️ Funcionalidades

- Buscar estacionamientos cercanos (Google Maps / Mapbox)
- Reservas anticipadas y pagos integrados
- Sistema de puntuaciones y reseñas
- Modo offline (PWA) y dark mode
- Panel administrativo con métricas en tiempo real

---

## 🐳 Configuración rápida (Dev)

Requiere tener instalado: Docker + Docker Compose

```bash
# Clonar el proyecto
git clone https://github.com/tu_usuario/parking-app.git
cd EasyParkingCL
