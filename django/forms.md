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

## Django form class definition
```
# forms.py in app named 'contact'
from django import forms

class ContactForm(forms.Form):
      name = forms.CharField(required=False)
      email = forms.EmailField(label='Your email')  
      comment = forms.CharField(widget=forms.Textarea)
```
>> There's no specific location Django expects forms to be in. You can equally place Django form classes in their own file inside an app (e.g. **forms.py**) or place them inside other app files (e.g. models.py, views.py). You can later import Django form classes to where they're needed, just like Django views or Python packages.

## Django view method that uses a Django form
```
# views.py in app named 'contact'
from django.shortcuts import render
from .forms import ContactForm

def contact(request):
    form = ContactForm()
    return render(request,'about/contact.html',{'form':form})
```

## Django form instance rendered in template as HTML
```
{{ form.as_table }}
{{ form.as_p }} 
{{ form.as_ul }}
```
## Django view method that sends and processes Django form
```
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = ContactForm(request.POST)
        # check if it's valid:
        if form.is_valid():
            # process data, insert into DB, generate email,etc
            # redirect to a new url:
            return HttpResponseRedirect('/about/contact/thankyou')
    else:
        # GET, generate blank form
        form = ContactForm()
    return render(request,'about/contact.html',{'form':form})
```
## Django form instance with initial argument declared in view method
```
def contact(request):
        ....
        ....
    else:
        # GET, generate blank form
        form = ContactForm(initial={'email':'johndoe@coffeehouse.com','name':'John Doe'})
        # Form is now initialized for first presentation to display these values
    # Reference form instance (bound/unbound) is sent to template for rendering
    return render(request,'about/contact.html',{'form':form})
```
## Django form fields with initial argument
```
from django import forms

class ContactForm(forms.Form):
      name = forms.CharField(required=False,initial='Please provide your name')
      email = forms.EmailField(label='Your email', initial='We need your email')
      comment = forms.CharField(widget=forms.Textarea)

def contact(request):
        ....
        ....
    else:
        # GET, generate blank form
        form = ContactForm()
        # Form is now initialized for first presentation and is filled with initial values in form definition
    # Reference form instance (bound/unbound) is sent to template for rendering
    return render(request,'about/contact.html',{'form':form})
```
