# Function: a block of code which executes only when its called

def my_function():
    print("Hello, This is my function")
    print("have a great day")
my_function()
my_function()

def full_name(x,y):
    print(f"My Name is {x} {y}")
full_name("Bhanu","pooja")

def hello(name):
    print(name+"pooja")
hello("bhanu")

def name(firstname, lastname):
    print("hello",firstname+" "+lastname)
name("Bethala","Bhanupooja")

#return: functions send python values/objects back to the caller. These values/objects are known as the function's return value
def multiply(num1,num2):
    result = num1 * num2
    return result
z = multiply(2,4)
print(z)