# Portal Web Modular: Noticias y Cine

Proyecto de Programación Back End (TI3041), Evaluación Sumativa 2. Mantiene los módulos Django `noticias` y `cine`, con persistencia MySQL en AWS, consultas ORM, relaciones entre entidades y administración CRUD en Django Admin.

Consulta [DOCUMENTACION_IA.md](DOCUMENTACION_IA.md) para revisar el uso de IA, su alcance y los archivos de migración entregados.

## Estado desplegado

- Sitio: http://44.223.101.218/
- Noticias: http://44.223.101.218/noticias/
- Cine: http://44.223.101.218/cine/
- Django Admin: http://44.223.101.218/admin/
- phpMyAdmin: http://44.223.101.218/phpmyadmin/
- Repositorio: https://github.com/ttinviboi/Proyecto_EvaluacionSumativa2
- Datos de demostración actuales: 6 noticias en 4 categorías y 6 películas en 3 géneros.

La instancia EC2 ejecuta Ubuntu, Django con Gunicorn detrás de Nginx, Apache/phpMyAdmin y MySQL. La aplicación se sirve en HTTP; las credenciales y claves no deben compartirse ni incluirse en el repositorio. El archivo `.env` privado está excluido por `.gitignore`; el ZIP contiene únicamente `.env.example`.

## Funcionalidades

- Listados, fichas y búsqueda por título para noticias y películas usando Django ORM.
- Entidades relacionadas: `Categoria` → `Noticia` y `Genero` → `Pelicula` mediante `ForeignKey`.
- Django Admin permite crear, visualizar, buscar, modificar y eliminar las cuatro entidades.
- Los botones Agregar, Modificar y Eliminar del sitio público son marcadores visuales para la siguiente evaluación; la pauta reserva la gestión funcional para Django Admin.
- Los comandos `cargar_noticias` y `cargar_peliculas` importan los JSON de `data/` de forma repetible.

## Estructura

- `mi_proyecto/`: configuración, ajustes y rutas principales.
- `noticias/`: modelo de categorías y noticias, vistas, administración, migraciones y carga inicial.
- `cine/`: modelo de géneros y películas, vistas, administración, migraciones y carga inicial.
- `templates/`: plantilla compartida.
- `static/`: Bootstrap e imágenes locales.
- `data/`: datos de demostración en JSON.

| Modelo / tabla | Relación | Uso |
|---|---|---|
| `Categoria` / `noticias_categoria` | Uno a muchos con `Noticia` | Clasificar publicaciones |
| `Noticia` / `noticias_noticia` | FK a `Categoria` | Contenido del portal |
| `Genero` / `cine_genero` | Uno a muchos con `Pelicula` | Clasificar películas |
| `Pelicula` / `cine_pelicula` | FK a `Genero` | Cartelera de cine |

Las migraciones iniciales están en `noticias/migrations/0001_initial.py` y `cine/migrations/0001_initial.py`. Django crea además sus tablas internas de usuarios, permisos, sesiones e historial de administración.

## Ejecutar localmente

Requisitos: Python compatible con el proyecto y pip.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Configura en `.env` una `SECRET_KEY` privada; para SQLite usa `DB_ENGINE=sqlite3`. Después:

```powershell
python manage.py migrate
python manage.py cargar_noticias
python manage.py cargar_peliculas
python manage.py createsuperuser
python manage.py runserver
```

Abre `http://127.0.0.1:8000/noticias/`, `/cine/` y `/admin/`. En Linux o macOS activa con `source .venv/bin/activate`.

## Obtener el código desde GitHub

El repositorio distribuye el proyecto dentro de un ZIP versionado. Para obtener la entrega mediante Git:

```bash
git clone https://github.com/ttinviboi/Proyecto_EvaluacionSumativa2.git
cd Proyecto_EvaluacionSumativa2
unzip Proyecto_EvaluacionSumativa2_Completado.zip
cd Proyecto
```

Después configura el entorno local siguiendo la sección anterior. El repositorio incluye README y commits; al presentar, muestra el historial con `git log --oneline` y el remoto con `git remote -v`.

## Base de datos y Django Admin

En la instancia, MySQL contiene `noticias_categoria`, `noticias_noticia`, `cine_genero` y `cine_pelicula`, además de las tablas internas de Django. Las vistas consultan estos datos mediante ORM. En phpMyAdmin, selecciona `evaluacion_sumativa2` para revisar tablas, filas y llaves foráneas. En `/admin/` puedes administrar noticias, categorías, películas y géneros.

Para la instancia real, `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` y `DB_*` se definen en un `.env` privado fuera del repositorio. No reutilices contraseñas incluidas en conversaciones o documentación; rótalas después de la evaluación y no autentiques phpMyAdmin por HTTP en redes no confiables.

## Evidencias de evaluación

El informe técnico incluye capturas del sitio, AWS EC2, las migraciones y servicios, Django Admin, GitHub y phpMyAdmin/base de datos. La revisión presencial debe mostrar en vivo la instancia, el historial y remoto Git, y las operaciones CRUD de Django Admin.

## Uso de inteligencia artificial

Se utilizó IA como apoyo para contrastar la pauta con el proyecto, identificar brechas, completar documentación y preparar datos de demostración. Las respuestas se aplicaron al código y se verificaron contra la estructura de modelos, migraciones y despliegue.


## Evaluación Sumativa 3: acceso y gestión

La aplicación añade inicio y cierre de sesión, paneles diferenciados, gestión de cuentas por perfil, mantenedores propios para categorías y géneros, y reservas que relacionan usuario y película. La interfaz administrativa se implementa con Django Templates y formularios; Django Admin no está habilitado como ruta de la aplicación. Revisa [DOCUMENTACION_IA.md](DOCUMENTACION_IA.md) para los prompts y el uso documentado de IA.

### Perfiles y permisos

- **Administrador:** acceso a los paneles, usuarios, mantenedores, eliminación y operación completa de reservas.
- **Supervisor:** consulta/creación/edición de categorías y géneros, consulta de reservas y actualización de su estado. No elimina registros ni gestiona usuarios.
- **Administrativo:** crea reservas y consulta únicamente sus propias reservas; no entra a mantenedores ni a gestión de cuentas.

Los grupos y permisos se inicializan al ejecutar las migraciones. `python manage.py crear_perfiles` permite recrear los grupos. El primer superusuario funciona como administrador. Desde su panel puede crear cuentas Supervisor y Administrativo, asignando el grupo correspondiente.

### Recuperación de contraseña por correo

Django genera tokens de un solo uso con su flujo integrado. Para desarrollo, el correo se imprime en la consola con `EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend`. Para recibirlo en una bandeja real, define SMTP en el `.env` privado; por ejemplo:

```env
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_HOST_USER=cuenta_smtp
EMAIL_HOST_PASSWORD=secreto_smtp
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=portal@example.com
```

No guardes contraseñas SMTP ni de usuarios en GitHub. En la instancia de AWS debe configurarse un proveedor SMTP autorizado antes de demostrar recepción real del mensaje.

### Nueva transacción y migración

`gestion.Reserva` relaciona al usuario autenticado y una película, registra fecha, cantidad y estado, evita reservas duplicadas para la misma función y restringe fechas pasadas. Su migración es `gestion/migrations/0001_initial.py`. Ejecuta:

```bash
python manage.py migrate
python manage.py crear_perfiles
python manage.py createsuperuser
python manage.py runserver
```

Entra por `/cuentas/ingresar/`; el panel principal está en `/`. La recuperación comienza en `/cuentas/recuperar/`. Los dos mantenedores están en `/categorias/` y `/generos/`; las reservas en `/reservas/`.
