"""
OOP stands for Object Oriented Programming 
A class is a blueprint we use to create objects
A class has the following properties:
 1.A constructor-This is special method(class function)vused to create a class object
 2.An attribute:These are variables declared in the scope of the class,as part of the class.
 3.A method-These are functions that are created inside the class as part of the class.We create them by adding a special parameter self,as their first parameter.
 
 Inititalization:This is the creating of an object from a class constructor
 
 PILLARS OF OOP
 1.Abstraction:This is the hiding of the complex logics implemented for a particular objective in the form of an object.
 2.Inheritance:A class can retain the properties of another class e.g their attribute and methods.
 3.Encapsulation:This is the regulation of access and modification of a class properies eg attributes and methods
 4.Polymorphism:used to implement the nature of another class without inheiritng its properties.

"""

# def is used when creating a function

class Animal:
     def __init__(self): #constructor    
        self.name="lion"
        self.food_character="carnivorous"
        self.family="mammal"
        
     def makes_sound(self):
        return "roar"
     def get_hobby(self):
        return "hunting and laughing"
    
animal_object=Animal()
print(animal_object.name)
print(animal_object.food_character)
print(animal_object.family)

print(animal_object.makes_sound())
print(animal_object.get_hobby())


class Animal:
     def __init__(self,name,food,family,sound,hobby): #constructor    
        self.name=name
        self.food_character=food
        self.family=family
        self.sound=sound
        self.hobby=hobby
        
     def makes_sound(self):
        return self.sound
     def get_hobby(self): 
        return self.hobby
    
animal1=Animal("tiger","carnivorous","mammal","roar","hunting")
print(animal1.name)
print(animal1.food_character)
print(animal1.family)

print(animal1.makes_sound())
print(animal1.get_hobby())

animal2=Animal("chicken","omnivorous","mammal","clacks","digging and gathering")
print(animal2.name)
print(animal2.food_character)
print(animal2.family)

print(animal2.makes_sound())
print(animal2.get_hobby())







    