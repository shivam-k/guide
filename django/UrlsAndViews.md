Urls
----
* How Django processes a request?
* ```url()``` vs ```path()```
* urlpatterns should be a Python list of ```path()``` and/or ```re_path()``` instances.
* Use ```re_path()``` instead of ```path()``` to use regex.
* Specifying defaults for view arguments
* Customizing error views
* Including other URLconfs: urlpatterns can “include” other URLconf modules

#### Django url parameter definition for access in templates

```
urlpatterns = [
    url(r'^drinks/(?P<drink_name>\D+)/',TemplateView.as_view(template_name='drinks/index.html')), 
    path('<int:question_id>/', views.detail, name='detail'),
]
```
* The value of **drink_name** from **<drink_name> & **question_id** from **<question_id>** can be accessed in ```veiws.py``` and also in ```Template```.
  * value of ```\D+``` is assigned to **drink_name** & of **int** to **question_id**
  * Value in **template** through ```{{ drink_name }}``` can be accessed, and in **view** through ```def detail(request, question_id):```
* ```url(r'^stores/',stores_views.detail,{'location':'headquarters'})``` URL extra options
* ```def detail(request,store_id='1',location=None):``` Deault Values in views
* Django url parameters are always treated as strings

#### Django view method extracting url parameters with request.GET
```
def detail(request,store_id='1',location=None):
    # Access store_id param with 'store_id' variable and location param with 'location' variable
    # Extract 'hours' or 'map' value appended to url as
    # ?hours=sunday&map=flash
    hours = request.GET.get('hours', '')
    map = request.GET.get('map', '')
    # 'hours' has value 'sunday' or '' if hours not in url
    # 'map' has value 'flash' or '' if map not in url
    return render(request,'stores/detail.html')
```

#### URL consolidation through include()

#### Url naming and namespaces


Writing Views
-------------
* View function takes Web request (Httpequest) and returns Web reponse (HttpResponse). This reponse can be anything: HTML, a redirect, a 404 error, an XML document, an image, etc. 
* Returning errors: The Http404 exception (commonly)
* For direcly rendering template in url:
```
from django.views.generic import TemplateView
from coffeehouse.about import views as about_views     #to avoid confusion in multiple views
urlpatterns = [
  url(r'^temp$', TemplateView.as_view(template_name='base.html')),
]
```
  
