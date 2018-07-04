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
## Accessing form values: request.POST and cleaned_data
* Data in ```request.POST``` are treated as srings, so pass them through ```cleaned_data```. (Can't access **cleaned_data** until  **is_valid** is called on the form.
```
form.cleaned_data['name'] to access **name** value.
```
## Validating form values : is_valid(), validators, clean_<field>() and clean()
 * #### Django form is_valid() method for form processing
   * Calling ```is_valid()``` also creates the ```cleaned_data``` dictionary on the form instance to hold the form field values that passed validation rules.
   * Calling ```is_valid()``` also creates the ```errors``` dictionary on the form instance to hold the form errors for each of the fields that didn't pass the validation rules.
 ```
 def contact(request):
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = ContactForm(request.POST)
        # Reference is now a bound instance with user data sent in POST
        # Call is_valid() to validate data and create cleaned_data and errors dict
        if form.is_valid():
           # Form data is valid, you can now access validated values in the cleaned_data dict
           # e.g. form.cleaned_data['email']
           # process data, insert into DB, generate email
           # Redirect to a new URL
           return HttpResponseRedirect('/about/contact/thankyou')
        else:
           pass # Not needed 
           # is_valid() method created errors dict, so form reference now contains errors 
           # this form reference drops to the last return statement where errors 
           # can then be presented accessing form.errors in a template
    else:
        # GET, generate blank form
        form = ContactForm()
        # Reference is now an unbound (empty) form
    # Reference form instance (bound/unbound) is sent to template for rendering
    return render(request,'about/contact.html',{'form':form})
 ```
 * #### Django form field validators option with custom validator method for form processing
   * you can equally reuse the custom validate_comment_word_count() method on any other form field in the same form or in another Django form through the validators option. In addition, you can also apply multiple validators to a field since the validators option accepts a list of validators.
 
 ```
 from django import forms
import re

def validate_comment_word_count(value):
      count = len(value.split())
      if count < 30:
            raise forms.ValidationError(('Please provide at least a 30 word message,
	    %(count)s words is not descriptive enough'), params={'count': count},)

class ContactForm(forms.Form):
      name = forms.CharField(required=False)
      email = forms.EmailField(label='Your email')
      comment = forms.CharField(widget=forms.Textarea,validators=[validate_comment_word_count])
 ```
* #### Django form field validation with clean_<field>() methods
 
 ```
 from django import forms

class ContactForm(forms.Form):
      name = forms.CharField(required=False)
      email = forms.EmailField(label='Your email')
      comment = forms.CharField(widget=forms.Textarea)
      def clean_name(self):
          # Get the field value from cleaned_data dict
          value = self.cleaned_data['name']
          # Check if the value is all upper case
          if value.isupper():
             # Value is all upper case, raise an error
             raise forms.ValidationError("""Please don't use all upper 
                  case for your name, use lower case""",code='uppercase')
          # Always return value 
          return value
      def clean_email(self):
          # Get the field value from cleaned_data dict
          value = self.cleaned_data['email']
          # Check if the value end in @hotmail.com
          if value.endswith('@hotmail.com'):
             # Value ends in @hotmail.com, raise an error
             raise forms.ValidationError("""Please don't use a hotmail email,
                                    we simply don't like it""",code='hotmail')
          # Always return value 
          return value
 ```
 * #### Django form field validation with clean() method
 
 ```
 from django import forms

class ContactForm(forms.Form):
      name = forms.CharField(required=False)
      email = forms.EmailField(label='Your email')
      comment = forms.CharField(widget=forms.Textarea)
      def clean(self):
          # Call clean() method to ensure base class validation 
          super(ContactForm, self).clean()
          # Get the field values from cleaned_data dict
          name = self.cleaned_data.get('name','')
          email = self.cleaned_data.get('email','')
          # Check if the name is part of the email
          if name.lower() not in email:
             # Name is not in email , raise an error
             raise forms.ValidationError("Please provide an email that contains your name, or viceversa")
 ```
 
 ## Django form field types: Widgets, options and validations
 * Refer for the different fields and their default widgets
 * Built-in widgets:
 ```
 PasswordInput, HiddenInput, MultipleHiddenInput, Textarea, CheckboxSelectMultiple, SelectDateWidget, SplitHiddenDateTimeWidget, FileInput
 ```
* By default, all Django form fields are marked as required. (for not ```none``` or empty string ```''```, ```required=False```)

#### Error messages: error_messages
#### Field layout values: label, label_suffix, help_text
