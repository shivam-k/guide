django/mysite/mysite
# Outer mysite/ = root dir, container for project.
# Inner mysite/ =  Real Project

# Put virtualenv parallel to mysite(outer):container
# Name 'mysite'(outer) can be changed


python3 --version

#Create Container Folder: 'mysite-container'
makdir django
cd django


# Virtual Environment
python3 -m venv myvenv #virtualenv called 'myvenv' parallel to mysite-container
source myvenv/bin/activate

# Installing Django
pip install --upgrade pip  #upgrade pip
pip install django
python -m django --version

# Start Project
django-admin startproject mysite #will create 'mysite/mysite', inner mysite being the real Project Folder

cd mysite

# Runserver
python manage.py runserver

# Startapp
python manage.py startapp polls

# Migrations
python manage.py makemigrations polls # send into the file
python manage.py migrate #implement in database

python manage.py sqlmigrate polls 0001
python manage.py check
python manage.py shell

# Admin
python manage.py Createsuperuser



