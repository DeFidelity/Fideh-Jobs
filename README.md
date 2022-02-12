# Fideh-Jobs

 Collaboration joint and job board modeled after Upwork.
 ![dashboard](https://user-images.githubusercontent.com/68183305/153730610-bb992833-0fa9-4683-abb5-37d7f2404aef.png)


## Description

This project is a server side rendered web-app that is fully inspired by Upwork and I start thinking about it when one of my mentor told me to go on there and pick a job up, I like what the platform does and as someone that needs idea for his portfolio project I seize the opportunity.
I went all out for this project and I learnt allot while building it, and I'm really glad I did.

![homepage](https://user-images.githubusercontent.com/68183305/153730628-98b6d9ce-e918-4ba9-be3a-ec5c9728700f.png)

## Language, Frameworks and Library

- Python
- Django
- Alpine JS
- HTMX
- Tailwind CSS
- HTML

## Features
![chat](https://user-images.githubusercontent.com/68183305/153730637-e93697d1-0587-43d1-97ef-0b7ade10c89d.png)

This project has allot of features and the highlights are:
- Authentication (Login, Logout and Register)
- Sign up as either Job applicant or Employer
- Managerial Dashboard (Helps manage all the jobs a user created or applied for)
- Messaging ( Communication between and employer and employee not user to user )
- Job Creation
- Job application
- Notification ( for new messages and new application)
- ....

## Installation and How to use
To install or use this project, you'll need to have Python installed with pip or pip 3 enabled, once that's done, clone this repository and open in an idea then run `pip install -r requirements.txt` to install all the project dependencies.
Once that's done, run `python manage.py makemigrations` and `pytjon manage.py migrate` to migrate all everything in the migration folders to an SQLite db. After that the project should be ready then run `python manage.py runserver` then navigate to the browser with Django prescribed localhost url provided.

## Credits
Library used in this project include:
- Django Tailwind
- Django HTMX
- Django Allauth
