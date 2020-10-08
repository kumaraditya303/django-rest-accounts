
Django Accounts
===============

Accounts is a Django app built on Django Rest Framework for easier account management for REST apps.

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
path('accounts/', include('polls.urls')),
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
