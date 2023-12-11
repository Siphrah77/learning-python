"""
INHERITANCE
-This is the process where a class acquires the properties of another class.
-This class that acquires the properties of another is referred to as the child class whereas the class whose properties are being acquired is referred to as the parent class.

"""
class Mammal:
    def __init__(self):
        self.no_of_legs=4
        self.blood="Warm blooded"
        self.skin_cover="furry"
        self.common_hobby="Noise Making"
    
    def get_common_hobby(self):
        return self.common_hobby
    
class CatFamily(Mammal):
    def __init__(self):
        super().__init__()
        self.food="carnivorous"
        
        
    def get_food(self):
        return self.food
"""
    Explanation
    -The first class,mammal is the parent class.
    -The second class,catfamily in this case is the child class
    -Catfamily inherits the properties of the mammal class.In python the syntax used to represent a child inheriting from a parent during defination is:
    
    class ChildClass(ParentClass)
    
    Eg:
    class CatFamily(Mammal)
       ...
       
   We can be able to access all Mammal properties even inside the CatFamily and even if we create a CatFamily object.
    
    
    """
    
cat_obj = CatFamily()
print(cat_obj.get_common_hobby())