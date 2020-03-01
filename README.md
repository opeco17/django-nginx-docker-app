# What are these codes?
These codes ara test framework for django application by nginx.

Please run below codes if you want to try it.

```
git clone https://github.com/opeco17/django-nginx-docker-app.git
```
```
docker-compose run python ./manage.py makemigrations prediction
```
```
docker-compose run python ./manage.py migrate
```
```
docker-compose run python ./manage.py collectstatic
```
```
docker-compose up -d
```

# Development Environment

Application : Django

App Server : uWSGI

Web Server : Nginx

Container : Docker
