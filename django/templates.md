* Support for template engines
* The Django template language (DTL)

DTL
----
* A template is rendered with a context. Rendering replaces variables with their values, which are looked up in the context (a dict-like object mapping keys to values), and executes tags. Everything else is output as is.
* Variables: {{ and }}. Dictionary lookup, attribute lookup and list-index lookups are implemented with a dot notation:
```
{{ my_dict.key }}
{{ my_object.attribute }}
{{ my_list.0 }}
```
* Tags: provide arbitrary logic in the rendering process. {% and %}
* Filters: transform the values of variables and tag arguments. {{ django|title }}
