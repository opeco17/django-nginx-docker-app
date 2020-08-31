# Language Prediction Application
This is the machine learning application which predicts what language your name comes from.

<img src="https://user-images.githubusercontent.com/46510874/74896505-cc5de100-53d7-11ea-814c-be00277a4354.png" width="80%">

<img src="https://user-images.githubusercontent.com/46510874/74896471-b3553000-53d7-11ea-82e6-384a530a29c4.png" width="80%">


# Technologies

Python/Django/PyTorch/SQLite/Nginx/uWSGI

# How to use 
Clone files from GitHub.
```
git clone https://github.com/opeco17/language-prediction-application.git
```
These below commands are for setting up the application.
```
docker-compose run application ./manage.py makemigrations prediction
```
```
docker-compose run application ./manage.py migrate
```
```
docker-compose run application ./manage.py collectstatic
```
Build docker image and run docker container. Please execute command on the place where Dockerfile exists.
```
docker-compose up -d
```
Please jump to below link and you will see above GUI.

http://localhost:8000/
