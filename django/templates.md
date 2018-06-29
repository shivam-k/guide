* Support for template engines
* The Django template language (DTL)
* Jinja template (in addition)
DTL
----
* A template is rendered with a context. Rendering replaces variables with their values, which are looked up in the context (a dict-like object mapping keys to values), and executes tags. Everything else is output as is.
* Variables: {{ and }}. Dictionary lookup, attribute lookup and list-index lookups are implemented with a dot notation:
```
{{ my_dict.key }}
{{ my_object.attribute }}
{{ my_list.0 }}
```
* **Tags:** provide arbitrary logic in the rendering process. {% tag %}
>> {% if %} ...... {% endif %},
>> {% for %} ..... {% endfor %},
* **Filters:** Modify variable for display. {{ django|title }}; Chained FIlter: {{ text|escape|linebreaks }} 
>> {{ value|default:"nothing" }},
>> {{ value|length }},
>> {{ value|filesizeformat }},

60 built-in filters are available; and even custom template Tags and Filters are available.

Template Inheritance
--------------------
The most powerful – and thus the most complex – part of Django’s template engine is template inheritance. Template inheritance allows you to build a base “skeleton” template that contains all the common elements of your site and defines blocks that child templates can override.
* ```{{block.super}} ``` :  get the content from the parent template block
* ```{% include "footer.html" %}``` 

* 
```
{% extends "base.html" %} 
{% block title %}{% endblock %} #put the code in between
```

* 
```
{% if %} ...... {% endif %}
{% for %} ..... {% endfor %}
{{ name }} for variable

{{ name|lower }}  #filter: convert to lowercase
{{ my_list|first|upper }} #take the first element in the list & convert it to uppercase
```

