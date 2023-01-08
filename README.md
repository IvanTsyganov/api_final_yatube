# api_final_yatube
**This is a final project of second quart in python developer course
by yandex-practicum**

I've prepared next features:

- Jdango project with custom models, views and urls

- REST API with CRUD functions

- JWT-Token Authentication

# How to start it:
1. fork this project
2. Open terminal and clone this repository:
```
git clone https://github.com/yandex-praktikum/api_final_yatube.git
```
2. create and start virtual environment(windows):
```
python -m venv venv
```
```
. venv/Scripts/activate
```
3. Install dependencies from requirements.txt
```
pip install -r requirements.txt
```
4. Make migrations:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
5. Start project:
```
python manage.py runserver
```