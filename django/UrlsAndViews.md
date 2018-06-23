Urls
----
* How Django processes a request?
* ```url()``` vs ```path()```
* urlpatterns should be a Python list of ```path()``` and/or ```re_path()``` instances.
* Use ```re_path()``` instead of ```path()``` to use regex.
* Specifying defaults for view arguments
* Customizing error views
* Including other URLconfs: urlpatterns can “include” other URLconf modules

Writing Views
-------------
* View function takes Web request (Httpequest) and returns Web reponse (HttpResponse). This reponse can be anything: HTML, a redirect, a 404 error, an XML document, an image, etc. 
* Returning errors: The Http404 exception (commonly)
