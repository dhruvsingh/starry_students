Starry Students
===============

Prerequisites
-------------
- Install docker_.
- Install docker-compose_.
- Uses cookiecutter-django_ for boilerplate.

.. _docker: https://docs.docker.com/get-docker/
.. _docker-compose: https://docs.docker.com/compose/install/
.. _cookiecutter-django: https://cookiecutter-django.readthedocs.io/en/latest/

Deployment
----------

The following details how to deploy this application.

::

$ [sudo] docker-compose -f local.yml up

Usage
-----


- Getting students and teachers using graphql
- Navigate to http://localhost:8000/graphql and run the following query:

::

    query {
       allTeachers{
        id
        name
        students{
          id
          name
        }
      }
    }


- [Un]Starring a student using graphQL
- Pass starredStudent as false to unstar, and true to star.
- teacherId and studentID are required, to depict which teacher is trying to [Un]Star which student.

::

    mutation {
      updateStar(starredStudent: false, teacherId: 4, studentId: 4){
        tsObj {
          id
          starredStudent
          student {name}
          teacher {name}
        }
      }
    }


- Query to get all teachers and their starred students

::

    query {
       starredStudents{
        teacher{
          id
          name
        }
        student{
          id
          name
        }
      }
    }

Helpful commands
-----------------

- Add an app (might need sudo), then do a chown -R on the folder created

::

$ sudo docker-compose -f local.yml run --rm django python manage.py startapp manager

- Add migration for student model

::

$ sudo docker-compose -f local.yml run --rm django python manage.py makemigrations manager --name add_student_model

- Add a superuser

::

$ sudo docker-compose -f local.yml run --rm django python manage.py createsuperuser

- Add a superuser

::

$ sudo docker-compose -f local.yml run --rm django python manage.py createsuperuser

- Connecting to postgres on docker

::

$ sudo docker-compose -f local.yml run --rm postgres psql -U <username from .envs/.local/.postgres/> -h postgres -p 5432 -d starry_students -W <password from .envs/.local/.postgres/>
