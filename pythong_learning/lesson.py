# this is a comment
#they are notes for you as a programmer
# comments are ignored by python
print("hello, world!") # this line prints a message to the screen
# variables store information for later use
name = "Emiliano" # storing a string in a variable
# string variables are normally enclosed in quotes
age = 15    # storing an integer in a variable
# integers are whole numbers with decimal points
height = 6.0 # storing a float in a variable
#floats are numbers with decimal points
is_student = True # storing a boolean in a variable
# booleans represent True or False values
# printing the variab;es
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)
#concatenating strings is what we do to join
#variables together for display
#its represented by the + symbol
print("Hello my name is " + name + ", I am " + str(age) + 
      "years old, my height is " + str(height) +
      " feet, and it is " + str(is_student))

#f-strings are another way to format strings
print(f"Hello, my name is {name}, I am {age} 
      years old, my height is 
      {height} feet, and it is {is_student}")
#create five more variables of different types
city = "Chicago"                # string variable
temperature = 53                # float variable
is_raining = False              # boolean variable
num_friends = 10000000000       # integer variable
favorite_food = "tacos"         # string variable
#print the new variables using f-strings