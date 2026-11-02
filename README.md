# Proyecto Evaluación Sumativa 3

Aplicación Django de Noticias y Cine con inicio de sesión, roles, recuperación de contraseña, mantenedores CRUD, reservas y persistencia relacional.

## Código y documentación

La instancia desplegada de referencia es http://44.223.101.218/.

- Código fuente: [Proyecto/](Proyecto/)
- Paquete listo para descargar: [Proyecto_EvaluacionSumativa3_Completado.zip](Proyecto_EvaluacionSumativa3_Completado.zip)
- Guía de instalación, perfiles y ejecución: [Proyecto/README.md](Proyecto/README.md)
- Documentación del apoyo de IA: [Proyecto/DOCUMENTACION_IA.md](Proyecto/DOCUMENTACION_IA.md)
- Migración de reservas: [Proyecto/gestion/migrations/0001_initial.py](Proyecto/gestion/migrations/0001_initial.py)
- Migraciones del dominio: `Proyecto/noticias/migrations/` y `Proyecto/cine/migrations/`

El proyecto usa `.env.example` como plantilla. Nunca publiques `.env`, credenciales SMTP ni contraseñas de usuarios. La recuperación por correo requiere credenciales de un proveedor SMTP; el backend de consola es únicamente para desarrollo local.
