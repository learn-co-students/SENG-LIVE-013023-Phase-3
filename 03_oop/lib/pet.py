# !/usr/bin/env python3
    # Defines the location of the Python interpreter
    # See More => https://stackoverflow.com/a/7670338/8655247

import ipdb

# Classes

# 1. ✅ Create a Pet class

    # Note: Add 'pass' to the Pet class

# Blueprint / Cookie Cutter Tray
class Pet:
    # pass

# 2. ✅ Instantiate a few Pet instances

    # Compare the Pet instances. Are each of them the same object?

        # No, they are not the same objects in memory, but they are created from the same
        # mold.

            # ipdb> spot
            # <lib.pet.Pet object at 0x10fd49520>
            # ipdb> fido
            # <lib.pet.Pet object at 0x10fdee7c0>

# 3. ✅ Demonstrate __init__ 
    def __init__(self, name, age, breed, temperament, owner="No Owner"):
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament
        self.owner = owner

    # fido = Pet()
    # *** TypeError: __init__() missing 4 required positional arguments: 'name', 'age', 'breed', and 'temperament'

    # Add arguments to instances  

    # Attributes:
        # name
        # age
        # breed
        # temperament
        # owner
    
    # Use dot notation to access each Pet instance's attributes 

    # Update attributes with new values

# Instance Methods

# 4. ✅ Create a "print_pet_details" function that will print each Pet instance's 
# attributes

    # Review the "self" keyword 

    def print_pet(self):
        print(self)
    
    # Invoke "print_pet_details" on an instance 
    
    def print_pet_details(self):
        print(f'''
            name: {self.name}
            age: {self.age}
            breed: {self.breed}
            temperament: {self.temperament}
        ''')

    # Example Terminal Ouput:
        # name: Rose
        # age: 11
        # breed: Domestic Longhair
        # temperament: Sweet

# 5. ✅ Create an Owner class with two instance methods:

class Owner:
    
    # def __init__(self, name, age):
    #     self.age = self.set_age(age)
    #     self.name = self.set_name(name)

    def set_age(self, age):
        if((type(age) == int) and (18 <= age <= 100)):
            self._age = age

        else:

            return "Age must be a number between 18 - 100"

    def get_age(self):
        print(self._age)

    # get_name => Retrieve Owner's name
    def get_name(self):    
        print(self._name)

    # set_name => Set Owner's name

        # Ensure that Owner's name is a String

        # If not, issue warning of "Name must be a string"

    def set_name(self, name):
        
        # If "name" that's passed in is a String...
        if(type(name) == str):
            
            # ...we can safely assume that this is acceptable
            # to set for our instance.

            self._name = name

        else:

            return "Name must be a string!"

    # Instance Properties

    name = property(get_name, set_name)
    age = property(get_age, set_age)

    # Use property() to compile get_name / set_name and invoke them
    # whenever we access an Owner instance's name

    # Object Properties => Attributes that are controlled by methods