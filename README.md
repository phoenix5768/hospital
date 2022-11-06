# hospital
Software Engineering Project

There is only 1 predefined admin:
- username: admin
- password: admin
 
Except for login and main page user cannot view every other pages, unless he is registered as an administrator.

Front-end of the project is not ready yet (as my partners responsible for front-end could not finish their part)

In this prototype, I did not yet finish the Update and Delete buttons (for both doctors and patients), but they will be done soon

There is one small problem, when you first login as an administrator you cannot see the tuples of the tables (for some reason). In order to see these tuples you have to press either "register patient" or "registor doctor" buttons and go back to the admin page. This problem will be fixed soon, as soos as I understand how to fix it :)

Project was written in Django Framework. Database was handled by sqlite3.

In order to run the project, type in the terminal "python manage.py runserver" and go to the link shown in the terminal.
