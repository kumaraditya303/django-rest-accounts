![Travis CI](https://img.shields.io/travis/com/kumaraditya303/django-rest-accounts?label=Travis%20CI&logo=travis&style=flat-square)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fkumaraditya303%2Fdjango-rest-accounts&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
![](https://img.shields.io/pypi/pyversions/djangorestaccounts?logo=Python&style=flat-square)
![](https://img.shields.io/pypi/dm/djangorestaccounts)
![](https://img.shields.io/codecov/c/github/kumaraditya303/django-rest-accounts?logo=codecov&style=flat-square)

Django Rest Accounts
===============

 Django Rest Accounts is a Django app built on Django Rest Framework for easier account management for REST apps.

Quick Start
-----------

- Add `accounts` to your INSTALLED_APPS like this::

```python
INSTALLED_APPS = [
    ...,
    "accounts",
]
```

- Include the accounts URLconf in your project urls.py like this::

```python
path('accounts/', include('accounts.urls')),
```
- In your settings.py set the 
```python
AUTH_USER_MODEL = "accounts.User"
```

- Run `python manage.py migrate` to create authentication models.

- Start the development server and visit http://127.0.0.1:8000

- URL Configuration

| URLConf       |               |
|:-------------:|:-------------:| 
| LOGIN         | /login/       | 
| REGISTER      | /register/    | 
| LOGOUT        | /logout/      | 

# Project made and maintained by Kumar Aditya
