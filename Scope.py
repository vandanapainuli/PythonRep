x = 300

def myfunc():
  x = 200
  print(x)
  global y=420

myfunc()  # This will print 200, the local x

print(x)  # This will print 300, the global x
print(y)  # This will print 420, the global y