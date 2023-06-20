# Meta Backend Certification Module 8: Capstone project

## Week 1: Setting up the environment

* Install VS code https://code.visualstudio.com/Download
* Install Python
https://www.python.org/downloads/
* Install Git

### Setup virtual environment with pipenv

$ pip3 install pipenv

$ pipenv //-> check if virtual environment installed

$ pipenv shell //-> activate virtual environment

## Install django

$ pipenv install django

$ django-admin startproject littlelemon .

* Go to Pipfile inside the main directory and update the package dependencie:

[packages]
django = "*"
djangorestframework = "*"
djangorestframework-xml = "*"
djoser = "*"

$ python manage.py startapp restaurant

$ python manage.py runserver //--> to ensure django and virtual environment setup

ctrl+C //--> exit server

## Week 2: Django database configuration and Models
### Connect to MySQL

$ pipenv install mysqlclient //--> adds mysqlclient as dependency

$ pipenv install //--> update all dependencies

### Configurate settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'littlelemon',
        'HOST':'127.0.0.1',
        'PORT':'3306',
        'USER':'root',
        'PASSWORD':'',
        'OPTIONS':{
            'init_command':"SET sql_mode ='STRICT_TRANS_TABLES'"
        }
}
INSTALLED_APPS =[
    'restaurant'
]

### Access MySQL through VS Code

* Install MySQL extension from VS Code extension marketplace: MySQL by Jun Han

$ python manage.py makemigrations

$ python manage.py migrate

* MySQL should be on the VS code explorer menu.  Click + to get access to database LittleLemon.
### Create Database and Connect to MySQL through MySQL command line

* Log into MySQL command line

$ CREATE DATABASE database_name;

$ SHOW DATABASES;

$ USE database_name;

$ show tables;

$ describe table; //--> see details of the table

* Create user for the database;

$ CREATE USER 'admindjango'@'localhost' IDENTIFIED BY 'employee@123!' ;

$ SELECT user FROM mysql.user //--> to ensure your user has been created

$ GRANT ALL ON *.* TO 'admindjango'@'localhost';

$ FLUSH PRIVILEGES; //--> update the user's access to all tables

$ exit; //--> exit MySQL

* Update settings.py with correct user and password;

### Setting up models: Booking and Menu

### Register Booking and Menu on admin.py, then access admin on browser

$ python manage.py createsuperuser
Username: admin
email address: admin@littlelemon.com
password: LittleLemon123!

$ python manage.py runserver

* go to server /admin, then login

## Week 2: Adding APIs

### Set up the menu API

$ pip3 install djangorestframework

* Configurate settings.py

INSTALLED_APPS =[
 ‘restaurant’,
 ‘rest_framework’,
]

### Set up the table booking API

## Week 3: Security and Testing

### User Authentication
* To use token-based DRF authentication 

Step 1: Configurate settings.py

INSTALLED_APPS =[
    'rest_framework.authtoken',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':[
        'rest_framework.authentication.TokenAuthentication',
    ]
}

Step 2: make migrations

* Add the registration page using Djoser authentication library and modify the existing user's credential from within the app instead of the admin interface

Step 1: Install djoser

$ pipenv shell //--> activate virtual environment

$ pipenv install djoser

Step 2: Configurate settings.py
--> settings.py
INSTALLED_APPS = [
    'djoser'
]

DJOSER = {
    'USER_ID_FIELD':'username',
    'LOGIN_FIELD':'email', //--> to set username as email
}

REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': [
  'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
}

Step 3: Enable djoser endpoints by adding the following URL routes in the project's URL patterns.

* add following lines to update urlpatterns list
path('auth/', include('djoser.urls')),
path('auth/', include('djoser.urls.authtoken'))

Step 4: Run the migration to create the token field in admin

$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver

### Securing the table booking API

Step 1: Add the 'rest_framework.authtoken' app to the list of INSTALLED_APPS in the settings.py file

Step 2: Import the IsAuthenticated class from the rest_framework.permissions module in the views.py file.

Step 3: You already have the BookingViewSet class in the views.py file. To secure this view, set the permission_classes property to a list containing IsAuthenticated.

permission_classes = [IsAuthenticated]

Step 4: Open the app's urls.py and import the following function:


* import obtain_auth_token view
from rest_framework.authtoken.views import obtain_auth_token

In the same file add a new URL route to the urlpatterns list:

* add following line in urlpatterns list
path('api-token-auth/', obtain_auth_token)

### Adding unit test
Step 1

When you create the app, an empty test.py file is created in the app package folder. Go ahead and delete it.

In the project container folder, create a new folder with the name tests.

Step 2

* Create files inside of test folder:
    __init__.py  //--> this allows python to identify the root folder
    test_urls.py
    test_views.py
    test_models.py


Step 3: python manage.py test to run all test

### Testing API using Insomnia
