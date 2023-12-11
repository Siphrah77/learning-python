
"""
Encapsulation helps regulate access and modification of class properties e.g attributes and methods.
Methods and Attributes can take the following characteristics
1.public:This means that they are accesible inside and outside the class.When we create an object of the class we are able to access its attribute and methods.
2.Private:This means that they are accesible only inside the class,we cannot access these methods and attributes.We di this to inform we want to protect e.g:apikey/appid attributes,password field etc.
3.protected: TODO :

If you want to make an attribute/method to be private you add two underscores '__' just before the actual name of an attribute or method.

Example 1:Attribute
self.__private attribute=value
E.g self.__WEATHER_APP_ID='your_id_here'

Example 2:
SYNTAX
def __your_private_method(self):
     ....
eg:def __prepare_params(self):

importance of encapsulation 
1.Concealing data-Eg appid that we wouldnt want the public accessing and modifying
2.Introducing read only attributes  
3.Introducing write only attributes

Introduction to Getters and Setters
>They are mainly public methods.

Getters
>A getter is a method that is used to fetch the value of a particular class attribute.It is mainly used to expose the value of a private attribute.
Eg.If we have a private attribute called national_id,we want it to be in such a way that we are able to see the value but we cannot change it.

-->So we can create a getter method which will return the value of our national_id.The benefit with using a getter method for this is that we wont be able to modify the value of the national_id externally
Syntax:Getter methods start with the key prefix 'get' followed by the name of the attribute whose value we want.

Eg:
def get_national_id(self):
    return self.__national_id #assuming  the private attribute was declared
    
Setters
-->They are used to control the modification of a private attribute.Eg modificatin of a password.
-->Unlike the getter method,they do not return anything,however they take up a users value of the private attribute to be modified as a parameter.

SYNTAX:They start with the key suffix 'set' followed by then name of the private attribute to be modified.

Example 
def set_password(self,modified_password) 
    set.__password=modified_password # Assuming the private attribute was declared
    
-->In the example above,the modified_password parameter is what will carry the users modified password

i.e:my_class_obj.set_password("new password")


"""