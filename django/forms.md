* ```GET``` & ```POST```: tow most common HTTP methods
* ```Form Class```: Same as models in Django.
  * Define fields
  * Use ```is_valid()``` method
  * ```Cleaned_data()```
  * View to catch the from data
 
* ```Widget class```: Each field type has an appropriate default **Widget class**, but these can be overridden as required.
* ```form classes```: are created as subclasses of either ```django.forms.Form``` or ```django.forms.ModelForm```. 
* **Bound** and **unbound** form instances
* Whatever the data submitted with a form, once it has been successfully validated by calling **is_valid()** (and is_valid() has returned True), the validated form data will be in the ```form.cleaned_data``` dictionary.
* ```ModelForm```: let deal with model directly
 * Each model field has a corresponding default form field. For example, a CharField on a model is represented as a CharField on a form. A model ManyToManyField is represented as a MultipleChoiceField
