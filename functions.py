#normal function without inputs
def my_function():
    print("Hello")
    print("Bye")


# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


def greet():
  print("Hello")
  print("How are you?")
  print("I'm good")
  
# greet()

# function that allow input

# def greet_with_name(name):
#   print(f"Hello {name}")
#   print(f"How are you {name}?")
#   print("Isn't the weather nice today?")

# greet_with_name("Vlad")

#functions with more than one input

def greet_name_location(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_name_location(location = "Nowhere", name = "Vladis")


name = input("What is your first name? ")
last_name = input("What is your last name? ")

def format_name(f_name, l_name):
  """capitalizes the given input of names."""
  formated_f_name = f_name.title()  #returns an output.
  formated_l_name = l_name.title()
  return f"{formated_f_name} {formated_l_name}"
formated_string = format_name(name, last_name)
print(formated_string)

