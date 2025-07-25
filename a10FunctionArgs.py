def PatientInfo(**myinfo) :
# i dont know what all is part of my info it can be name, age sex etc
    print("Patient Information :\n My name is  "+myinfo["name"]+" and I a am "+str(myinfo["age"])+" years old and I live in "+myinfo["address"])
PatientInfo(sex="Female", age=25, address="India", name="Anjali")

# This Part code accepts dynamic input from the user for patient information and displays it.
name=input("Enter your name: ")
age=input("Enter your age: ")
print("Patient Information :when values accepted dynamically")


PatientInfo(name=name, age=age, address=address)