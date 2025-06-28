# variable Scope: the region that a variable can be accessed

name = "bhanu" #global scope variable (accessed inside and outside of a function)
def display_name():
    name = "pooja" #local scope variable (accessed only inside of a function
    print("my name is "+name)
display_name()
print("my name is "+name)