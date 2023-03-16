import ipdb

# 1. ✅ First Class Functions
# "[We can] assign them to variables, store them in data structures, pass them as arguments
# to other functions, and even return them as values from other functions."
# See more => http://bit.ly/3YQh8KR

    # Create functions to be used as callbacks 

# def walk(pet):
#     print(f"{pet} Walked!")

# def feed(pet):
#     print(f"{pet} Fed!")

    # Create a higher-order function that will take a callback as an argument

# def execute_task(func):
#     func("Rose")

# ipdb.set_trace()

# 2. ✅ Create a higher-order function that declares / returns an inner function

# Higher-Order Function
# def higher_order_function():
    
#     # Inner Function
#     def inner_function():
#         print("Hello From Within!")

#     return inner_function

# ipdb.set_trace()

def execute_task():
    def walk(pet):
        print(f"{pet} Walked!")    

    return walk

walk = execute_task()

# walk("Rose")

# 3. ✅ Decorator

# Create a decorator (coupon_calculator) that:
    # DONE - takes a function as an argument
    # DONE - has an inner function defined 
    # DONE - returns the inner function

# Tools:

    # .format()
    # https://www.geeksforgeeks.org/python-string-format-method/

    # .round()
    # https://www.geeksforgeeks.org/round-function-python/

# Create Decorator (coupon_calculator)
def coupon_calculator(func):
    
    # Responsible for Reporting Price Back
    def report_price():
        print("Initial Price = $35.00")
        
        # Invoke passed in function to compute price
        final_price = func(35.00)
        
        # Report Newly Discounted Price Back to User
        print(f'Newly Discounted Price: ${final_price}')

    return report_price

# Create Callback Function to Calculate New Price (calculate_price)

# If we apply a 50% discount, we should a number that 
# represents a Dollar Amount

    # $35.00 => $17.50

# def calculate_price(price):
    
#     # :.2f => Format Price as 2 Decimal Point Floating Number
    
#     return '{:.2f}'.format(round(price / 2, 2))

# Try using a decorator with / without pie syntax '@'

# Without pie syntax 

# report_price = coupon_calculator(calculate_price)
# report_price()

# With pie syntax

    # @decorator
    # def cb_function():
        # ...

    # cb_function()

@coupon_calculator
def calculate_price(price):
    
    # :.2f => Format Price as 2 Decimal Point Floating Number
    
    return '{:.2f}'.format(round(price / 2, 2))

calculate_price()