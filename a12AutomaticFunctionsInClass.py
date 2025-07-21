class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)

#this _str_ method is used to print the object in a readable format. if you just print object and dont specify what variable in that object, then this will print  the objects as specified here
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"
print("Demonstation of __str__ method in class Person")
p1 = Person("John", 36)

print(p1)