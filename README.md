# Adhira_api_assignment

This is a Django REST Framework-based backend that provides APIs for managing **Bogie Checksheets** and **Wheel Specifications**. It uses **MySQL** as the database and supports filtering capabilities for efficient data retrieval.

##  Features

## Bogie Checksheet
- **POST** `/forms/bogie-checksheet` – Submit new bogie inspection data.
- **GET** `/forms/bogie-checksheet-list` – Retrieve all submitted bogie inspection records.

## Wheel Specification
- **POST** `/forms/wheel-specifications` – Submit new wheel specification data.
- **GET** `/forms/wheel-specifications` – Retrieve wheel specifications. Supports filters:
  - `bogie_number`
  - `inspection_date`

##  Tech Stack

- **Backend**: Django, Django REST Framework
- **Database**: MySQL
- **Filtering**: `django-filter`

### Setup Instructions

## Environment Setup

pip install virtualenv
python -m venv myenv
# Activate virtual environment
.\myenv\Scripts\activate


## Install Dependencies

pip install django
pip install djangorestframework
pip install python-dotenv
pip install mysqlclient
pip install django-filter

## Project Setup

django-admin startproject apibackend
cd apibackend
python manage.py startapp formsapi

## Migrate and Run

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

## Note  

Make sure your settings.py is configured

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
