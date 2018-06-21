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

#************ Model Data Access
from polls.models import Question, Choice
from books.models import Publisher

>>> q = Question(question_text="What's new?", pub_date=timezone.now())
>>> q.save()

>>> p = Publisher.objects.create(..............)  #auto save

>>> Question.objects.all() # objects.all() displays all the questions in the database

>>> Question.objects.filter(id=1) #Returns a QuerySet, as in list
>>> Publisher.objects.filter(country="U.S.A.", state_province="CA")

>>> Question.objects.get(id=1) #Retrieve single objects
>>> Publisher.objects.get(name="Apress")

>>> Publisher.objects.order_by("name") # (-name) for reverse ordering
>>> Publisher.objects.order_by("state_province", "address")


#***********Creating Relationships
#Create an article
>>> a = Article(id=None, headline="This is a test", pub_date=date(2005, 7, 27), reporter=r) #diff way 
>>> a.save()

#Create an article by the reporter object
>>> new_article = r.article_set.create(headline="John's second story", pub_date=date(2005, 7, 29)) #r being the class Reporter

#Create a new article, and add it to the article set:
>>> new_article2 = Article.objects.create(headline="Paul's story", pub_date=date(2006, 1, 17))
>>> r.article_set.add(new_article2)

>>> Article.objects.all() # all articles
>>> r.article_set.all() #r being reference to one reporter
>>> q.article_set.all() #q being reference to another reporter



#************** Template
{% if %} ...... {% endif %}
{% for %} ..... {% endfor %}
{{ name }} for variable

{{ name|lower }}  #filter: convert to lowercase
{{ my_list|first|upper }} #take the first element in the list & convert it to uppercase
