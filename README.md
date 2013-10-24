csmanager
=========

Test Django project to manage Server and their Client.

Install
=======

The first thing to do install dependencies

```
sudo apt-get install postgresql python-dev build-essential postgresql-contrib python-psycopg2
```

When we can set our clear virtualenv. The path of Django project may be ~/Projects, /opt/, /usr/local/
It's very important to the security of web application.

```
virtualenv /path/to/venv/  --no-site-packages
source /path/to/venv/bin/activate
```

You will switch to this virtual environments, but can't have some packages to run Django project.
Run the next command to get the packages needed to run our project. All version of package is set in
requirements.txt. And you can change it to another if you have any troubles.

```
pip install -r requirements.txt
```

When we need to install database backend. In this example I use PostgresSQL database.

```
sudo su - postgres

createdb django_db

# Role name: django_login
# Pass: django
createuser --username=postgres -SDRP  

logout
```

You may use another database name and user name, but don't forget to change the settings.py in the
project folder in the DATABASES dict.

```
cd /path/to/venv/
git clone git@github.com:hummermania/csmanager.git
cd csmanager
```
 
 This clone the project from github. And you can run the develop server

 ```
 python manage.py syncdb
 ```

 You will be asked that you don't have any superuser defined. Accept this and enter some
 superuser name, email and pass. For example:
    name: root
   email: root@mail.ru   ;-)
    pass: root

Congratulations!!! You can try to run our developer server

```
python manage.py runserver
```

  If in the prev step you can't have some errors - you can open the URL http://localhost:8000/ in
  the browser and see the main page of project. If you see some error - please create new issue in Issue page on this project.

  When go to http://localhost:8000/admin/ and use authorisation info what you set in 'syncdb'
  command. In the admin page you can create some group and user in this group what can login into the admin part.
  Set for this user permission to enable create, editing and delete "core-client" item. It will allow to some user
  work on client, and move it from/to another server.
