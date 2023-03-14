# Sequence Types
    
# Note: use print() to execute the examples. Comment out examples as needed to keep your Terminal
# output clean.

# Creating Lists
#1. ✅ Create a list of 10 pet names
pet_names = ['Rose', 'Meow Meow Beans', 'Mr.Legumes', 'Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini', 'Paul']

# Reading Information From Lists
#2. ✅ Return the first pet name
# print(pet_names[0])

#3. ✅ Return all pet names beginning from the 3rd index

# Will Include Element With Index of 3
# print(pet_names[3:])

#4. ✅ Return all pet names before the 3rd index

# Will Not Include Element With Index of 3
# print(pet_names[:3])

#5. ✅ Return all pet names beginning from the 3rd index and up to / including the 7th index
# print(pet_names[3:8])

#6. ✅ Find the index of a given element => .index()
# print(pet_names.index("Luke"))

#7. ✅ Reverse the original list => .reverse()

    # reverse() => Destructive Method
    # Demonstrates that Lists are Mutable (Changeable)

# return_val = pet_names.sort(reverse=True)
# return_val = pet_names.reverse()

# print(return_val)
# print(pet_names)

#8. ✅ Return the frequency of a given element => .count()

# print(pet_names.count("Luke"))

# Updating Lists
#9. ✅ Change the first pet_name to all uppercase letters => .upper()

    # .upper() => Non-Destructive
    # Return Value => None

# return_val = pet_names[0].upper()

# print(return_val)
# print(pet_names)

#10. ✅ Append a new name to the list => .append()

    # .append() => Destructive
    # Return Value = New / Modified Array

# pet_names.append('XYZ')
# print(pet_names)

#11. ✅ Add a new name at a specific index => .insert()

    # .insert() => Destructive
    # Return Value = New / Modified Array

# pet_names.insert(2, 'Bud')
# print(pet_names)

#12. ✅ Add two lists together => +
# print([1,2,3] + [4,5,6])

#13. ✅ Remove the final element from the list => .pop()

    # .pop() => Destructive
    # Return Value = The Element That Was Removed

# def print_removed_item(item):
#     print(item)

# var = pet_names.pop()
# # print(pet_names)

# print_removed_item(var)

#14. ✅ Remove element by specific index => .pop()

    # .pop(0) => Destructive
    # Return Value = The Element That Was Removed

# var = pet_names.pop(0)
# print(pet_names)
# print(var)

#15. ✅ Remove a specific element => .remove()

    # .remove(<SOME ELEMENT>) => Destructive
    # Return Value = None

# pet_names.remove("Rose")
# print(pet_names)

#16. ✅ Remove all pet names from the list => .clear()

    # .clear() => Destructive
    # Return Value = None

# pet_names.clear()
# print(pet_names)

# Break Point 

#Tuple
# 📚 Review:
    # Mutable, Immutable <=> Changeable, Unchangeable
    
    # Why Are Tuples Immutable?

        # What advantages does this provide for us? In what situations
        # would this serve us?

        # Tuples are useful for representing static (not dynamic / alterable) data.

        # Helps us to preserve our data.

#17. ✅ Create a Tuple of 10 pet ages => () 
# pet_ages = (1,2,3,4,5,6,7,8,9,10)

#18. ✅ Print the first pet age => []
# print(pet_ages[0])

# Testing Mutability 
#19. ✅ Attempt to remove an element with ".pop" (should error)

# pet_ages.pop()

    # AttributeError: 'tuple' object has no attribute 'pop'

#20. ✅ Attempt to change the first element (should error) => []

# pet_ages[0] = 2

    # TypeError: 'tuple' object does not support item assignment    

# Tuple Methods
#21. ✅ Return the frequency of a given element => .count()

# pet_ages = (1,2,2,2,3,4,5,6,7,8,9,10)
# print(pet_ages.count(2))

#22. ✅ Return the index of a given element  => .index()

# print(pet_ages.index(2))

    # Returns Index of First Occurrence of Argument

#23. ✅ Create a Range 
# Note:  Ranges are primarily used in loops

# my_range = range(60)

# for num in my_range:
#     print(num)

# Sets (Stretch Goal)
#24. ✅ Create a set of 3 pet foods
pet_fav_food = {'house plants', 'fish', 'bacon'}

# Dictionaries 
# Creating 
#25. ✅  Create a dictionary of pet information with the keys "name", "age" and "breed"

    # JSON Object

pet_info_rose = {'name':'Rose', 'age':11, 'breed':'domestic long'}


#26. ✅  Use dict to create a dictionary of pet information with the keys "name", "age" and "breed" => dict(...)
pet_info_spot = dict(name='Spot', age=25, breed='boxer')

    # Advantages => Less Keystrokes / Easier to Read Syntax

# Reading
#27. ✅ Print the pet attribute of "name" using bracket notation 

# pet_info_rose['temperament']

    # KeyError: 'temperament'

#28. ✅ Print the pet attribute of "age" using ".get"

    # Note: ".get" is preferred over bracket notation in most cases 
    # because it will return "None" instead of an error

    # .get() => Built In 

# return_val = pet_info_rose.get('temperament', "Attribute Not Found!")
# print(return_val)

# Updating 
#29. ✅ Update Rose's age to 12 => []
# pet_info_rose['age'] = 12

#30. ✅ Update Spot's age to 26 => .update({...})

    # .update() => Dictionary Method
        # Pass a Dictionary

# pet_info_spot.update({'age': 26})

# Deleting
#31. ✅ Delete Rose's age using the "del" keyword => []

    # del => Destructive
    # Nothing is Returned

# del pet_info_rose['age']

#32. ✅ Delete Spot's age using ".pop"

    # .pop() => Destructive
    # Return Value => Value of the Key / Value Pair That Was Deleted

#33. ✅ Delete the last item for Rose using "popitem()"

    # .popitem() => Destructive
    # Return Value => Tuple Containing (1st) Key Name and (2nd) Value Associated With Key

# pet_info_spot.popitem()

# Loops 
pet_info = [
    {
        'name':'Rose',
        'age':11,
        'breed': 'domestic long-haired',
    }, 
    {
        'name':'Spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Gracie',
        'age':2,
        'breed': 'domestic long-haired',
    }
]

#34. ✅ Loop through a range of 10 and print every number within the range


#35. ✅ Loop through a range between 50 and 60 that iterates by 2 and print every number


#36. ✅ Loop through the "pet_info" list and print every dictionary 


#37. ✅ Create a function that takes a list a parameter 
    # The function should use a "for" loop to loop through the list and print each item 
    # Invoke the function and pass it "pet_names" as an argument


#38. ✅ Create a function that takes a list as a parameter
    # The function should define a variable ("counter") and set it to 0
    # Create a "while" loop 
        # The loop will continue as long as the counter is less than the length of the list
        # Every loop should increase the count by 1
    # Once the loop has finished, return the final value of "counter"


#39. ✅ Create a function that updates the age of a given pet
        # The function should take a list of "dictionaries", "name" and "age" as parameters 
        # Create an index variable and set it to 0
        # Create a while loop 
            # The loop will continue so long as the list does not contain a name matching the "name" param 
            # and the index is less then the length of the list
            # Every list will increase the index by 1
        # If the dictionary containing a matching name is found, update the item's age with the new age 
            # Otherwise, return 'Pet not found'

# map like 
#40. ✅ Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase


# find like
#41. ✅ Use list comprehension to find a pet named spot


# filter like
#42. ✅ Use list comprehension to find all of the pets under 3 years old


#43. ✅ Create a generator expression matching the filter above

