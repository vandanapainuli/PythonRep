# DIR or HELP functions will help you know more about the modules. what functions or classes are available in the module
import datetime
print(dir(datetime))  
#when i run this code the list of function will appear in the terminal
#i want to see this in better way


import datetime

with open("datetime_functions.txt", "w") as f:
    f.write("\n".join(dir(datetime)))
#this creates a txt file where my python codes are saved. i can open via notepad or any text editor

#the other way to see contents of a module is to use help function
import datetime
help(datetime)
