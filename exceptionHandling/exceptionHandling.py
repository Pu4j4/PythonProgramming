# exception: events detected during execution that interrupt the flow of a program


try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator

except ZeroDivisionError as e:
    print(e)
    print("You cannot divide by zero! stupid")
except ValueError as e:
    print(e)
    print("enter only numbers please")
except Exception as e:
    print(e)
    print("something went wrong :(")
else:
    print(result)
finally:
    print("this will always execute")