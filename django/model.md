
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

Model Data Access
-----------------
* **Looksup**: Retrieving specific objects with filters: **filter(**kwargs)** & **exclude(**kwargs)**
    * **Field Lookups**: are how you specify the meat of an SQL WHERE clause. They’re specified as keyword arguments to the QuerySet methods **filter()**, **exclude()** and **get()**.
    * If you don’t provide a lookup type – that is, if your keyword argument doesn’t contain a double underscore – the lookup type is assumed to be exact. Both are same:
    ```
    >> Blog.objects.get(id__exact=14)  #Explicit form
    >> Blog.objects.get(id=14)         #__exact is implied
    ```
    * Many lookups are available: exact, iexact, contains, icontains, startswith, endswith, istartswith, iendswith
    * Lookups that span relationships

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

* Connecting posts to the questions, as for relationships, are done two ways:
      * 
      
        ```
        q = Question.objects.get(id=1) #Question by id=1
        Choice.objects.create(choice_text='Just Fine', votes=2, question=q) #question is key for relationship between bewteen QUestion & Choice.
        ```
        
        ```
        q = Question.objects.get(id=1) #Question by id=1
        q.choice_set.create(choice_text='Just Fine', votes=2) #Here QUestion key is not required in the argument.
        ```


Django Admin
-----------------
* The Django admin site provides a web based interface to access the database connected to a Django project. **CRUD** operations.
* Register & Configure Django models in ```admin.py```. Although you can technically use a single ```admin.py``` to register and configure all Django models -- just like you can have a single ```models.py``` to define all Django models -- it's a recommended practice that each Django app use its own ```admin.py``` file to manage its corresponding model defined in ```models.py```.

There are three ways to register a Django model for the Django admin in admin.py file: 

```
from django.contrib import admin
from coffeehouse.stores.models import Store

# Option 1 - Basic
admin.site.register(Store)    
                            
# Option 2 - Allows customizing Django admin behavior
class StoreAdmin(admin.ModelAdmin):
      pass
admin.site.register(Store, StoreAdmin)

# Option 3 -- Decorator
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
      pass
```

* ```__str__``` definition is primitive in models class.
* 
