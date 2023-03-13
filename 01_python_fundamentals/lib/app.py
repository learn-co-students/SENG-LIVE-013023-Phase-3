#!/usr/bin/env python3

# 📚 Review:
    # Python Environment Setup
	# Python Debugging Tools
	# Python Data Types 

# 🚨 To enable ipdb debugging, first import "ipdb"
import ipdb

# Python => snake_case 
# JavaScript => camelCaseEachNewWord

# JavaScript => Declare Variables Without Assignment
# Python => Cannot Declare Variables Without Assignment

# NameError: name 'pet_mood' is not defined

# 1. ✅ Create a condition to check a pet's mood
    # DONE => If "pet_mood" is "Hungry!", "Rose needs to be fed."
    # If "pet_mood" is "Rowdy!", "Rose needs a walk."
    # In all other cases, "Rose is all good."

    # Note => Feel free to set your own values for "pet_mood" to view various outputs.

pet_mood = "Rowdy!"
pet_name = "Rose"

# ipdb.set_trace()

# JavaScript => else if
# Python => elif

# if (pet_mood == "Hungry!"){
if pet_mood == "Hungry!":
    print("Rose needs to be fed!")
elif pet_mood == "Rowdy!":
    print("Rose needs to be walked!")
# elif pet_mood == "Feisty!":
#     print("Rose needs to be walked!")
# elif pet_mood == "Mischievous!":
#     print("Rose needs to be walked!")
# elif pet_mood == "Bored!":
#     print("Rose needs to be walked!")
else:
    print("Rose is all good!")


# 2. ✅ Create a ternary operator using "pet_mood" as a condition:
    # If pet_food is "Hungry!" => "Rose needs to be fed."
    # In all other cases => "Rose is all good."

# 3. ✅ Create a function (say_hello) that returns the string "Hello, world!"
    # Test invocation of "say_hello" in ipdb using "say_hello()"
    # say_hello() => "Hello, world!"

# 4. ✅ Create a function (pet_greeting) that will return a string with interpolated pet's name
    # Test invocation of "pet_greeting" in ipdb using "pet_greeting()"
    # pet_greeting("Rose") => "Rose says hello!"
    # pet_greeting("Spot") => "Spot says hello!"

# 5. ✅ Move conditional logic from Deliverable 1 into a function (pet_status) so that we may use it with different pets / moods
    # Test invocation of "pet_status" in ipdb using "pet_status(pet_name, pet_mood)"
    # pet_status("Rose", "Hungry!") => "Rose needs to be fed."
    # pet_greeting("Spot", "Rowdy!") => "Spot needs a walk."
    # pet_greeting("Bud", "Relaxed") => "Bud is all good."
    
    # Take a moment to note that "pet_name" and "pet_mood" parameters are within Local Scope and take priority over "pet_name" and "pet_mood"
    # in Global Scope.

# 6. ✅ Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors. 
    # If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user
    # pet_birthday(10) => "Happy Birthday! Your pet is now 11."
    # pet_birthday("oops") => "Type Error Occurred"

    # Note => To view more common Python exceptions, visit https://docs.python.org/3/library/exceptions.html

# 🚨 To create an ipdb breakpoint, comment / uncomment line below:
# ipdb.set_trace()


