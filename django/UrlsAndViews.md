Urls
----
* How Django processes a request?
* ```url()``` vs ```path()```
* urlpatterns should be a Python list of ```path()``` and/or ```re_path()``` instances.
* Use ```re_path()``` instead of ```path()``` to use regex.
* Specifying defaults for view arguments
* Customizing error views
* Including other URLconfs: urlpatterns can “include” other URLconf modules
* **TemplateView** (For direcly rendering template in url) & **RedirectView**:
```
from django.views.generic import TemplateView
from coffeehouse.about import views as about_views     #to avoid confusion in multiple views
urlpatterns = [
  url(r'^temp$', TemplateView.as_view(template_name='base.html')),
  path('go-to-django/', RedirectView.as_view(url='https://djangoproject.com'),
]
```
#### Django url parameter definition for access in templates

```
urlpatterns = [
    url(r'^drinks/(?P<drink_name>\D+)/',TemplateView.as_view(template_name='drinks/index.html')), 
    path('<int:question_id>/', views.detail, name='detail'),
]
```
* The value of **drink_name** from **<drink_name>** & **question_id** from **<question_id>** can be accessed in ```veiws.py``` and also in ```Template```.
  * value of ```\D+``` is assigned to **drink_name** & of **int** to **question_id**
  * Value in **template** through ```{{ drink_name }}``` can be accessed, and in **view** through ```def detail(request, question_id):```
* ```url(r'^stores/',stores_views.detail,{'location':'headquarters'})``` **URL extra options**
* ```def detail(request,store_id='1',location=None):``` **Deault Values in views**
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
* Django url using name
```
# Definition in urls.py 
url(r'^$',TemplateView.as_view(template_name='homepage.html'),name="homepage")

# Definition in view method
from django.http import HttpResponsePermanentRedirect
from django.core.urlresolvers import reverse

def method(request):
    ....
    return HttpResponsePermanentRedirect(reverse('homepage'))

# Definition in template
<a href="{% url 'homepage' %}">Back to home page</a>
```
* Django url with arguments using name


Views
-------------
* View function takes Web request (HttpRequest) and returns Web reponse (HttpResponse). This reponse can be anything: HTML, a redirect, a 404 error, an XML document, an image, etc. 
* Returning errors: The Http404 exception (commonly)
* ```request``` object, present in view method, contains information set by entities present before a view method: a user's web browser, the web server that runs the application or a Django middleware class configured on the application. Common attributes and methods available in a ```request``` reference:
```
request.method
request.GET or request.POST
request.POST.get('name', default=None)
request.GET.getlist('drink',default=None)
request.META
request.META['REMOTE_ADDR']
request.user
```
* Set up dictionary in Django view method for access in template
```
from django.shortcuts import render

def detail(request,store_id='1',location=None):
    # Create fixed data structures to pass to template
    # data could equally come from database queries
    # web services or social APIs
    STORE_NAME = 'Downtown'
    store_address = {'street':'Main #385','city':'San Diego','state':'CA'}
    store_amenities = ['WiFi','A/C']
    store_menu = ((0,''),(1,'Drinks'),(2,'Food'))
    values_for_template = {'store_name':STORE_NAME, 'store_address':store_address,
                           'store_amenities':store_amenities, 'store_menu':store_menu}
    return render(request,'stores/detail.html', values_for_template)
    
# In Template
<h4>{{store_name}} store</h4>
<p>{{store_address.street}}</p>
<p>{{store_address.city}},{{store_address.state}}</p>
<hr/>
<p>We offer: {{store_amenities.0}} and {{store_amenities.1}}</p>
<p>Menu includes : {{store_menu.1.1}} and {{store_menu.2.1}}</p>
```
#### View method responses
* the ```render()``` method is part of the ```django.shortcuts``` package. Alternatives are available.

#### View method middleware

#### Class-based views
