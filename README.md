# Paragraph

Blog application, developed with [Django](https://github.com/django/django) and [Django REST framework](https://github.com/encode/django-rest-framework), using [PostgreSQL](https://www.postgresql.org/).

Available on [paragraph-blog.herokuapp.com](https://paragraph-blog.herokuapp.com/)

> Use VPN to visit paragraph-blog.herokuapp.com


## documentation

Documentation: [ [swagger](https://paragraph-blog.herokuapp.com/api/schema/swagger-ui/) ] [ [redoc](https://paragraph-blog.herokuapp.com/api/schema/redoc/) ]

Schema: [ [schema](https://paragraph-blog.herokuapp.com/api/schema/) ]

## features

Authentication: users can create account and login to the application, based on token authentication.

Posts: create, read, update and delete functionalities has been implemented for posts. users can publish posts after authentication. edit and delete option of post are only available for its author.

Admin: dashboard implemented using django admin app which can be used to manage users, posts, etc.


## how to run

Run `python manage.py runserver` to start development server on `http://localhost:8000/`.

Run `python manage.py test` to execute tests.
