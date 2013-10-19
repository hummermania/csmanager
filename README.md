csmanager
=========

Test Django project to manage Server and their Client.

Install
=======

First install Django framework in your system, or virtualenv

'''
sudo pip install Django
sudo pip install django-annoying
'''

Make or change (if it exists) the directory where all Django web projects is located

'''
sudo mkdir /webapps
sudo chown user:user /webapps
'''
 where user - is your local user account.

When we need to install database backend. In this example I use PostgresSQL database.

'''
sudo apt-get install postgresql postgresql-contrib

sudo su - postgres

createdb django_db
createuser --username=django_login -SDRP 
logout
'''

On last command you will be promted for user password, say them:  django
You may use another database name and user name, but don't forget to change the settings.py in the
project folder in the DATABASES dict.

'''
cd /webapps
git clone git@github.com:hummermania/csmanager.git
cd csmanager
'''
 This clone the project from github. 
 You can run the develop server

 '''
 python manage.py createsuperuser  # for example: root:root
 python manage.py syncdb
 python manage.py runserver
 '''

 If in the prev step you can't have some errors - you can open the URL http://localhost:8000/ in 
 the browser and see the main page of project. If you see some error - please create new issue in Issue page on this project.

 When go to http://localhost:8000/admin/ and use authorisation info what you set in 'createsuperuser'
 command. In the admin page you can create some group and user in this group what can login into the admin part.
 Set for this user permission to enable create, editing and delete "core-client" item. It will allow to some user
 work on client, and move it from/to another server.
 


