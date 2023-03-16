import ipdb

# 7. ✅. Create a subclass of Pet called Cat
    
    # import Pet from lib.pet

from lib.pet import Pet

# Pet
    # Cat
    # Dog
    # Bird
    # ...

class Cat(Pet):

# 8. ✅. Create Cat class + __init__ that takes all the parameters from Pet and an
# additional parameter called indoor (Boolean)

    def __init__(self, name, age, breed, temperament, indoor):
        # self.name = name
        # self.age = age
        # self.breed = breed
        # self.temperament = temperament

        # Use super to pass the Pet parameters to the super class (DRY)
        super().__init__(name, age, breed, temperament)

        # Add an indoor attribute
        self.indoor = indoor

# 9. ✅. Create a method unique to the Cat subclass called talk which returns the string "Meow!"

    def say_meow(self):
        print(f'{self.name} says meow!')

# 10. ✅. Create a method called print_pet_details to match the print_pet_details in Pet    
        
        # Add super().print_pet_details() and print the indoor attribute

    def print_cat_details(self):
        # print(f'''
        #     name:{self.name}
        #     age:{self.age}
        #     breed:{self.breed}
        #     temperament:{self.temperament}
        # ''')
        
        super().print_pet_details()

        print(f'''
            Indoor: {self.indoor}
        ''')