
Fields:
-------
Only required and v.imp

Fields options: 
--------------
null, blank, choices, deault, help_text, primary_key, unique

Relationships: 
--------------
* ```on_delete``` to be considered
### Many-to-one
use django.db.models.ForeignKey as a Field type
* ```ForeignKey``` requires a positional argument: the class to which the model is related.

### Many-to-many
use ```ManyToManyField``` as a Field type
* It doesn’t matter which model has the ManyToManyField (don't put in both)
* Name of the ManyToManyField be plural as suggested
* ``` a1.publications.add(p1)``` Associate the Article(a1) with a Publication(p1)
* ```new_publication = a2.publications.create(title='Highlights for Children')``` Create and add a Publication to an Article in one step using create()

### One-to-one
use ```OneToOneField``` as a Field Type
* ```item = models.OneToOneField(Item,on_delete=models.CASCADE,primary_key=True)```
  * 
  >> Blog.objects.get(id__exact=14)  # Explicit form
  
  >> Blog.objects.get(id=14)         # __exact is implied

Model Data Access
-----------------
* Retrieving specific objects with filters: **filter(**kwargs)** & **exclude(**kwargs)**
    * **Field Lookups**: are how you specify the meat of an SQL WHERE clause. They’re specified as keyword arguments to the QuerySet methods **filter()**, **exclude()** and **get()**.

```
from polls.models import Question, Choice
from books.models import Publisher

q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()

p = Publisher.objects.create(..............)  #auto save

Question.objects.all() # objects.all() displays all the questions in the database

Question.objects.filter(id=1) #Returns a QuerySet, as in list
Publisher.objects.filter(country="U.S.A.", state_province="CA")

Question.objects.get(id=1) #Retrieve single objects
Publisher.objects.get(name="Apress")

Publisher.objects.order_by("name") # (-name) for reverse ordering
Publisher.objects.order_by("state_province", "address")
```


Creating Relationships
------------------------
* Create an article
```
a = Article(id=None, headline="This is a test", pub_date=date(2005, 7, 27), reporter=r) #diff way 
a.save()
```

* Create an article by the reporter object
```
new_article = r.article_set.create(headline="John's second story", pub_date=date(2005, 7, 29)) #r being the class Reporter
```

* Create a new article, and add it to the article set:
```
new_article2 = Article.objects.create(headline="Paul's story", pub_date=date(2006, 1, 17))
r.article_set.add(new_article2)
```

```
Article.objects.all() # all articles
r.article_set.all() #r being reference to one reporter
q.article_set.all() #q being reference to another reporter
```



Template
-----------------
