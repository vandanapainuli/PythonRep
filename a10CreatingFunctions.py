#def keyword is used to define a function
def greet(name):
    """This function greets the person passed in as a parameter."""
    #this line was a docstring-like a comment but it can be used as part of the code. it is stored as _doc_. i used it in line 7
    print("Hello, " + name + "!")   
# Call the function with a name
print("SO...."+greet.__doc__)  # Print the docstring of the function

greet("Amit")

#passing arbitrary arguments to a function. when we dont know how many arguments will be passed to the function, 
# we can use *args
# Parameters are what you define in the function, 
# and arguments are what you pass to the function when you call it.
#Both are same technically
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

# using default parameter value if function is called without argument
def my_function(country = "Norway"):
    print("Lets do Default parameter \n  I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


