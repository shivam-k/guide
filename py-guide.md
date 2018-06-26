Class
------
* ```__init__()method```: The first argument of every class method, including the __init__() method, is always a reference to the current instance of the class. By convention, this argument is named self. In all class methods, self refers to the instance whose method was called. But in the specific case of the __init__() method, the instance whose method was called is also the newly created object. Although you need to specify self explicitly when defining the method, you do not specify it when calling the method; Python will add it for you automatically.
* **Instantiating Class**: Instantiating classes in Python is straightforward. To instantiate a class, simply call the class as if it were a function, passing the arguments that the __init__() method requires. The return value will be the newly created object.
* **Instance Variable**:
