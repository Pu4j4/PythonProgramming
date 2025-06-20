#Logical operators (and,or,not)
#and: returns true if both conditions are true
#or: returns true if atleast one condition is true
#not: Reverse the result, returns False if the result is true

temp = int(input("What is the temperature outside?:"))
if temp >= 0 and temp <=30:
# if not(temp >= 0 and temp <= 30):
    print("the temperature is good today! Go outside")
elif temp == 0 or temp >30:
    print("The temperature is bad today! Stay inside")
else:
    print("enter valid value")
