#arrays are not built-in in python. We can use LISTs as arrays because they are built-in and more flexible.
# A list can have mix-type data too unlike arrays
#still we can use the ARRAY MODULE to create arrays
#Also via NUMPY we can create arrays

#Arrays as LIST
myList = [1, "Rain", 3, 4, 5]
print("This is the Array/List\n"+  str(myList))
#Accessing elements in a list
print(myList[1]+"  and number is "+ str(myList[3]) ) # First element


cars=["BMW", 12, "Mercedes", "Toyota", "Honda"]
for x in cars:
  print("the car is   ", x)
  #i used , instead of + this time so a number 12 was printed just like strings without converting anything
