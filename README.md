# 🚗 EasyParkingCL

**Encuentra, reserva y paga tu estacionamiento ideal usando IA, geolocalización y biometría.**  
EasyParkingCL es una plataforma inteligente (móvil y web) que conecta a conductores con los mejores lugares para estacionar según conveniencia, cercanía, tráfico en tiempo real y disponibilidad.

---

## 🌐 Visión General

> ¿Llegando al Portal Temuco o a un mall y no sabes dónde estacionar?  
> EasyParkingCL te guía al espacio más conveniente con ayuda de mapas, IA y sensores inteligentes.

---

## 📦 Estructura del Proyecto (Monorepo)

![image](https://github.com/user-attachments/assets/d2b9b6f7-81d5-4a73-9d72-1f59a9e26676)

---


---

## 🚀 Tecnologías

| Categoría          | Stack Tecnológico |
|--------------------|-------------------|
| **Frontend**       | React Native (Expo), React.js, TypeScript, Zustand, **TanStack Query**, TailwindCSS, Three.js |
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
- Verificación por código vía correo electrónico

---

## 🧠 Inteligencia Artificial

- 🔍 Recomendación automática del lugar ideal para estacionar
- 🎙️ Asistente por voz para buscar y reservar
- 📊 Predicción de demanda según horarios, sectores y eventos
- 🤖 Reconocimiento biométrico (voz, rostro, huella)

---

## 🗺️ Funcionalidades principales

- Buscar estacionamientos por cercanía, disponibilidad o precio
- Reservar y pagar online desde la app
- Visualización en 3D del mapa (Three.js)
- Panel administrativo (métricas, usuarios, reservas)
- Soporte PWA + Dark mode + modo offline

---

## 🐳 Configuración rápida para desarrollo

### 🔧 Requisitos

- Python 3.8.7
- Docker + Docker Compose
- Node.js + Yarn o npm
- Firebase CLI

---

### ⚙️ Backend

```bash
cd backend
python3 -m venv env
source env/bin/activate
cp .env.example .env
make docker-up
make migrate-local
make createsuperuser-local
make run-local


---


# 📱 EasyParkingCL – Frontend (Mobile App)

Aplicación móvil desarrollada con **React Native + Expo** que permite a los usuarios encontrar, reservar y pagar estacionamientos usando inteligencia artificial, geolocalización, biometría y mapas en tiempo real.

---

## 🚀 Tecnologías Principales

- **React Native (Expo)**
- **TypeScript**
- **Zustand** – Estado local global
- **TanStack Query** – Manejo de datos remotos / API
- **TailwindCSS (NativeWind)** – Estilizado moderno
- **Firebase** – Autenticación y notificaciones push
- **React Navigation** – Navegación entre pantallas
- **Three.js + expo-three** – Visualización 3D de mapas o zonas
- **AsyncStorage** – Persistencia de sesión y estado
- **Mapbox / Google Maps API** – Geolocalización y navegación

---

## 📁 Estructura de Carpetas

frontend/
├── components/ # Componentes UI reutilizables (atomic design)
├── screens/ # Pantallas de la app (Home, Login, Mapa, Reservas)
├── hooks/ # Hooks personalizados (auth, geolocalización, etc)
├── store/ # Zustand stores (estado global)
├── services/ # Lógica de API con TanStack Query
├── config/ # Temas, colores, constantes, endpoints
├── assets/ # Íconos, imágenes, fuentes
├── App.tsx # Punto de entrada de la app
└── ...



---

## 🔐 Autenticación

- Login tradicional: RUT o Email + contraseña
- Login con Google OAuth2
- Login biométrico:
  - Huella dactilar
  - Reconocimiento facial
  - Voz (futuro)
- Verificación por código (correo electrónico)
- Autenticación persistente con `AsyncStorage`

---

## 📦 Instalación del Proyecto

### Requisitos

- Node.js + npm
- Expo CLI (si no lo tienes: `npm install -g expo-cli`)
- App [Expo Go](https://expo.dev/client) en tu celular (iOS o Android)

### Pasos

bash
cd frontend
npm install
npm start


Se abrirá el Expo DevTools. Desde ahí puedes:

Escanear el QR con tu teléfono

O ejecutar en emulador:
npm run android o npm run ios (solo en macOS)

⚙️ Comandos Útiles
Comando	Descripción
npm start	Inicia el servidor Expo
npm run android	Lanza la app en un emulador Android
npm run ios	Lanza la app en emulador iOS (solo Mac)
npm run build	Construye la app (Expo EAS)
npm run lint	Ejecuta linter (si está configurado)
npm test	Corre tests (Jest/Testing Library)

🧠 Estado & Datos
Zustand (estado local):
Tema (oscuro/claro)

Sesión del usuario

Control de modales

Preferencias del usuario

TanStack Query (estado remoto):
Estacionamientos disponibles

Disponibilidad en tiempo real

Reservas creadas / canceladas

Historial de pagos y reservas

🌐 Geolocalización & Mapas
Integración con Google Maps API o Mapbox

Permisos de ubicación (Foreground + Background)

Cálculo de rutas óptimas (a futuro)

Vista de zona de estacionamientos en 3D (expo-gl + three.js)

🔔 Notificaciones Push
Usamos Firebase Cloud Messaging (FCM)

Envío de alertas:

Reserva confirmada

Estacionamiento pronto a vencer

Ofertas o sugerencias personalizadas

🧪 Testing
Si deseas testear:

bash
Copiar
Editar
npm install --save-dev jest @testing-library/react-native
npm test




🛠️ DevOps
CI/CD: GitHub Actions para testing y despliegue continuo

Infraestructura: Terraform + NGINX + certificados SSL

Contenedores: Docker + Docker Compose

Notificaciones push: Firebase Cloud Messaging (FCM)

📍 Roadmap
 Login con correo y Google

 Autenticación biométrica

 Dashboard web para administración

 Sensores IoT físicos (ocupación real)

 IA predictiva de ocupación por zona y horario

 Pagos vía Transbank y MercadoPago

👤 Autor
Pedro Pablo Osorio San Martín
📫 posoriosanmartin@gmail.com
🔗 https://github.com/PPOSM1993
