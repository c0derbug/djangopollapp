# Django Poll App
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

A simple polls application

## Requirements
- Python >= 3.5.2
- Django 2.2.10
- Django REST framework 3.11.0

## Installation
Install using pip...

```sh
pip install djangopollapp
```
Add the following to your settings.py module:

```sh
INSTALLED_APPS = [
    ...
    'djangopollapp',
]

MIDDLEWARE = [
    ...
    'polls.middleware.PollMiddleware',
]
```
Include polls api to your urls.py:

```sh
    # Polls API
    url('^api-polls/', include('polls.api.urls'))
```
and
```sh
./manage.py makemigrations
./manage.py migrate
```

## Testing the Setup

Example superuser authentication:
```sh
curl -X POST -d "username=<username>&password=<password>" http://127.0.0.1:8000/api-token-auth/

# Response from DRF
{"token":"dfaef188d5f075802cf7b627a41e4dd3632d127b"}%  
```

After that we can create poll without questions:
```sh
curl -X POST -H "Authorization: Token <token>" 
-H "Content-Type: application/json" 
-d '{"poll":
        {
            "title":"Sample",
            "end_date":"2021-05-13T21:25:46Z",
            "description":"sample discript"
        }
    }' http://127.0.0.1:8000/api-polls/v1/polls/
    
# Response axample
{
    "id":1,
    "author":1,
    "title":"Created-poll",
    "start_date":"2020-05-15T06:41:04.837196Z",
    "end_date":"2021-05-13T21:25:46Z",
    "description":"some descript",
    "is_active":true,
    "questions":[]
}
```

## Documentation