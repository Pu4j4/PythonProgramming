#Python weight converter

weight = float(input("Enter your weight: "))
unit = input("kilograms or pounds?(K or L): ")

if unit == "K":
    weight = weight * 2.205
elif unit == "L":
    weight = weight / 2.205
else:
    print(f"{unit} was not valid")

print(f"Your weight is: {weight} {unit}")