# Evaluación Técnica Full-Stack - Remesas App

Aplicación full-stack para gestión de remesas desarrollada con FastAPI, React, PostgreSQL y Docker.

---

## Stack utilizado

- Backend: FastAPI
- Frontend: React
- Base de datos: PostgreSQL
- ORM: SQLAlchemy
- Autenticación: JWT
- Infraestructura: Docker / Docker Compose

---

## Funcionalidades implementadas

- Registro de usuario
- Login con autenticación JWT
- Protección de rutas mediante token
- Crear remesas
- Listar remesas por usuario
- Eliminar remesas
- Persistencia de sesión con localStorage
- Conexión completa frontend-backend
- Base de datos relacional con integridad
- Paginación básica en backend

---

## Estructura del proyecto
fullstack-remesas/
├── backend/
│ ├── app/
│ │ ├── api/
│ │ ├── core/
│ │ ├── db/
│ │ ├── models/
│ │ ├── schemas/
│ │ └── main.py
│ ├── Dockerfile
│ └── requirements.txt
├── frontend/
│ ├── src/
│ └── package.json
├── docker-compose.yml
└── README.md

---

## Cómo ejecutar el proyecto

### 1. Levantar backend + base de datos

Desde la raíz del proyecto:

docker compose down
docker compose up --build


Backend disponible en:
http://localhost:8000


Documentación Swagger:
http://localhost:8000/docs


---

### 2. Levantar frontend

Abrir otra terminal:

cd frontend
npm install
npm start


Frontend disponible en:
http://localhost:3000


---

## Flujo de uso

### 1. Registrar usuario

POST `/auth/register`

{
"full_name": "Usuario",
"email": "test@test.com
",
"password": "123456"
}


---

### 2. Login

POST `/auth/login`

{
"email": "test@test.com
",
"password": "123456"
}


---

### 3. Crear remesa

POST `/remittances/`

{
"amount": 100,
"receiver_name": "Juan"
}


---

### 4. Listar remesas

GET `/remittances/`

---

### 5. Eliminar remesa

DELETE `/remittances/{id}`

---

## Decisiones técnicas

### API y resiliencia
Se evaluó el uso de una API externa para conversión de moneda. Para garantizar estabilidad en la entrega, se dejó el flujo funcional sin depender de servicios externos, evitando fallos por conectividad o límites de uso.

### Librerías utilizadas
- FastAPI: rapidez y documentación automática
- SQLAlchemy: manejo de base de datos relacional
- JWT (python-jose): autenticación segura
- React: interfaz de usuario
- Docker: entorno reproducible

### Arquitectura backend
Se utilizó una estructura por capas:
- api: endpoints
- models: base de datos
- schemas: validación
- db: conexión
- core: seguridad

Esto facilita mantenimiento y escalabilidad.

### Lógica de negocio
Cada remesa está asociada al usuario autenticado mediante `sender_id`, lo que garantiza que un usuario solo acceda a sus propios datos.

---

## Retos encontrados

- Configuración de Docker
- Manejo de CORS
- Integración frontend-backend
- Autenticación con JWT
- Alineación entre modelos y base de datos

---

## Mejora continua

Si se extendiera el proyecto:
- Integración real con API de tipo de cambio
- Dashboard con gráficas
- Manejo completo de roles (emisor/receptor)
- Edición de remesas
- Pruebas unitarias
- Mejoras de UI/UX

---

## Seguridad

- Contraseñas encriptadas
- Uso de JWT
- Rutas protegidas
- Validación con Pydantic
- Control de acceso por usuario

---

## Estado final

Proyecto full-stack funcional con autenticación, base de datos, operaciones CRUD y despliegue local mediante Docker.
