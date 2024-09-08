# djangoCourse
Web Personal - Proyecto Básico
Para poder clonar el repositorio es necesario activar el entorno virtual : pipenv shell

instalar las dependencias: 
pipenv install

hacer las migraciones y 
python manage.py migrate

crear el superusuario.
python manage.py createsuperuser

para los archivos estaticos:
docker-compose run django_app python webpersonal/manage.py migrate

docker-compose run django_app python webpersonal/manage.py collectstatic