# Django Interview Task

App I was asked for to do as a test for an interview

## Instructions

Clone this repisitory and cd into src.

```bash
git clone git@github.com:SleepNoMore/django_interview_task.git
cd django_interview_task/src
```

## Install requirements

```bash
pip install -r requirements.txt
```

## Run local server

```py
python manage.py runserver
```

## Endpoints

```url
localhost:8000/                         -Home page
localhost:8000/users                    -List of all the users
localhost:8000/users/details/<int:pk>   -Detail about specific user
localhost:8000/login                    -Login page
localhost:8000/register                 -Registration page
localhost:8000/admin                    -Django admin panel (for testing)
                                        -username:admin password:admin
```

## Task requirements

```text
Task 1:
Add to the user model new field, to store their unique employee identification (alphanumeric).
This field is not mandatory, and it should be read-only when user status is active.

Add field to list and form view.

Task 2:
In the form view of user, display user login count. We should be able to see how many times user logged in.
If necessary  add functionality to get how many times user tried to login (depends from Framework, as some of them already do have DB structure for this).

Task 3:
On user form view, add button "Login As", that button will execute functionality that we login as that user.
Only admins can see/execute this functionality.

```
