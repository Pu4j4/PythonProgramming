# Multiple Assignment: Allows us to assign multiple variables at the same time in one line of code

name = "Bhanu"
age = 21
attractive = True
print(name)
print(age)
print(attractive)
print("Name is: "+name+", "+"age is: "+str(age)+", "+"she is attractive: "+str(attractive))

#one line code
first_name, last_name, age, isAttractive = "Bhanu", "pooja", 21, True
print(first_name+last_name+" "+str(age)+" "+str(isAttractive))

#one line code with same value
# bhanu = 25
# casey = 25
# bob = 25
#Above assignment is equals to
bhanu = casey = bob = 25
print(bhanu+casey+bob)
