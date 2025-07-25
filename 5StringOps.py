#String is an Array in Pyton
a = "Hello, World!"
print(a[5])
#keyword 'in' and 'not in' in Python
txt = "The best things in life are free!"
print("beat" in txt)
txt = "The best things in life are free!"
print("beat" not in txt)
#slicing string in Python
txt = "The best things in life are free!"
print( txt[9:])
print( txt[9:16])
print(txt[:16])

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hellow, World!"
print(a.split("W")) # returns ['Hello', ' World!']
print(a.split("w")) # returns ['Hello', ' World!']
# concatenation
a = "Hej"
b= "Vandana"
c= a + " " + b
print(c) 
 #f-strings or Format strings -string combined with numbers
age = 36
txt = f"My name is John, I am {age}"
print(txt)
#Modifiers in f-strings
price = 59.6753
txt = f"The price is {price:.2f} dollars"
print(txt)
#escape characters
# this will give error: 
# txt="we are the so called "Vikings" of the north"
txt="we are the so called \"vikings\" of the north"
print(txt ) # This will cause a syntax error due to unescaped quotes

txt2="it's alright"
print (txt2) # This will work fine as the single quote is escaped