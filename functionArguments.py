# Arguments: the information is passed into function definition with help of arguments
# Keyword arguments: the information is passed using keyword while passing the values


def my_function(firstname,lastname,age):
    print("Hello "+firstname+" "+lastname+" "+str(age)+" years old")
my_function(firstname="bhanu",age=22,lastname="pooja")

#arbitrary arguments(*args): if the number of arguments are unknown,
# add a * before the parameter name
# This way the function will receive a tuple of arguments, and can access the items accordingly

def myfunc(*kids):
    print("The youngest child is "+kids[2])
myfunc("bhanu","mike","cherry")

def add(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum
print(add(1,2,3,4))

def myfun(food):
    for x in food:
        print(x)
fruits = ["apple","banana","cherry"]
myfun(fruits)

def func(x):
    return 2 * x
print(func(2))
print(func(7))

# **kwargs: if the number of keyword arguments are unknown,
# add ** before the parameter name
# This way the function will receive a dictionary of arguments, and can access the items accordingly

def keyArgs(**kwargs):
    print("his lastname is "+ kwargs["lname"])
    print("hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")
keyArgs(fname="john",lname="doe",middle="paul")

#default parameter value
def fun(country="india"):
    print("I am from "+ country)
fun("us")
fun()