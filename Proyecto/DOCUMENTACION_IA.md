# Documentación del uso de inteligencia artificial

## Herramienta y propósito

Se utilizó ChatGPT/Codex como apoyo para revisar la pauta de la Evaluación Sumativa 2, completar la documentación del proyecto Django y preparar contenido de demostración. La IA ayudó a identificar los componentes que debían quedar visibles para la revisión: modelos relacionales, migraciones, consultas ORM, administración, carga de datos y despliegue.

## Solicitud de trabajo registrada

> Revisa la pauta de la Evaluación Sumativa 2 y el proyecto Django adjunto; identifica brechas y complétalo para cubrir persistencia relacional, Django ORM/Admin, variables de entorno, navegación, evidencia y despliegue documentado.

## Aportes asistidos por IA

- Revisión de la estructura y contraste con los requisitos de evaluación.
- Apoyo en la implementación y documentación de los módulos `noticias` y `cine`, sus modelos relacionados y vistas con consultas ORM.
- Apoyo en los comandos para cargar los datos JSON de ejemplo y en la configuración documentada de Django Admin.
- Preparación de textos y registros de demostración para noticias y películas.
- Redacción de instrucciones de instalación, configuración mediante `.env`, migración y despliegue.

## Revisión y responsabilidad

El resultado se contrastó con la estructura del código, los modelos, las migraciones y el despliegue del proyecto. Las salidas de IA se trataron como propuestas que debían revisarse; el uso de IA no reemplaza la explicación del estudiante sobre el funcionamiento del código ni la demostración presencial. Los datos de noticias y películas son contenido de muestra.

## Archivos de migración incluidos

- `noticias/migrations/0001_initial.py`: crea `Categoria` y `Noticia`, incluida su relación mediante clave foránea.
- `cine/migrations/0001_initial.py`: crea `Genero` y `Pelicula`, incluida su relación mediante clave foránea.
- `noticias/migrations/__init__.py` y `cine/migrations/__init__.py`: identifican los paquetes de migración.

Para mostrar o aplicar las migraciones desde la carpeta `Proyecto/`:

```bash
python manage.py showmigrations
python manage.py migrate
```
