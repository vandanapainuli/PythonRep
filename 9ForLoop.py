# for loop in a list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print("The list has now--> "+ x)
  if x == "banana":
    break
#for loop in a string/skipping r in cherry
fruits = "cherry"
for x in fruits:
    if x == 'r':
        continue
    print("The string is -->   "+x)

#for loop with range() function. prints numbers in specified range example from 2 to 30 and increment each number by 3
i=0
for x in range(2,30,3):
    i+=1
    print("The Resultant range has "+str(i)+"th number as --> "+ str(x))
else:
    print("The for loop has completed its execution and the last number printed is --> "+ str(x))

#nested for loop example
STR1 = ["I love", "The smartest is"]    
STR2 = ["Amit", "Vandana", "Jwarna", "Shridhar"]

for x in STR1:
  for y in STR2:
    print(x, y)
