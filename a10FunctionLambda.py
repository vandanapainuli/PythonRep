#Lambda function can perform only 1 operation but i can pass ANY argument any number of times
x = lambda a:print (a) #it just prints A

x("Hello World")    #calling the lambda function with a string
x(420)              #calling the lambda function with a number

#Here i print after calling lambda function. Lambda function will take arguments and perform an operation
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#Lambda function better used inside other functions
def myfunc(n):
    return lambda a: a * n  
mydoubler = myfunc(2)# myfunc returns a lambda function which is stored in mydoubler. So mydoubler is now a function 
print(mydoubler(11)) #calling lambda function with 11 as argument.

#another example of lambda function inside a function

def make_prefixer(prefix):
    return lambda word: f"{prefix}{word}"

add_hello = make_prefixer("Hello, ")
print(add_hello("Vandana"))  # Output: Hello, Vandana


