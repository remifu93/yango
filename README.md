**Para iniciar el proyecto en local con docker**
- `docker-compose up --build`

**Para crear el super user de django dentro del contenedor**
- `docker-compose exec web bash`
- `python manage.py createsuperuser`

**Para inicializar el proyecto con poetry**
- `poetry install`