#if statement: a block of code which executes if given condition is true

# num = 20
# if num == 20:
#     print("the given number is:",num)
#
# #if-else: default block of code which executes if condition is not true
# if num == 21:
#     print("the given number is true")
# else:
#     print("the given number is not true")
#
# #elif: Allows for checking multiple conditions executes if conditions are true
# score = 90
# if score == 30:
#     print("Grade: F")
# elif score >= 90:
#     print("Grade: A")
# elif score <= 80:
#     print("Grade: B")
# else:
#     print("Grade: C")

age = int(input("How old are you?: "))
if  1<=age<=12:
    print("you're a kid")
elif 13<=age<=19:
    print("you're Teenage")
elif age>19:
    print("you're an adult")
else:
    print("you're not born yet")