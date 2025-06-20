# List: Lists are used to store multiple items in a single variable.
# List items are ordered, mutable or changeable, and allow duplicate values

# mylist = ["bhanu",  20, "student", 158.7]
# print(mylist)
# print(len(mylist))
# print(mylist[2])

# food = ["biryani", "kfc", "pastry", "fries", "pudding"]
# print(food)
# print(len(food))
# food[2] = "sambhar" #replaces the index[2] value with sambhar
# print(food)
#
# for x in food:
#     print(x)
#
# print(food[2])
# print(food[-1])
# print(food[2:4])
#
# if "kfc" in food:
#     print("yes, it is")
# else:
#     print("No")
#
# food.insert(4,"mutton")
# print(food)
#
# food.append("pastry")
# print(food)
#
# food1=["chicken fry","chicken lollypop","chicken 65"]
# food.extend(food1)
# print(food)
#
# food.remove("pudding")
# print(food)
#
# food.pop(4)
# print(food)
#
# food.sort()
# print(food)
#
# print(food.count("fries"))
#
# food.clear() #deletes entire list
# print(food)


#2D lists: a lists of lists

drinks = ["maaza", "coffee", "tea"]
dinner = ["pizza", "Burger", "sandwich"]
dessert = ["cake", "icecream", "apricot delight"]

foods = [drinks, dinner, dessert]
print(foods)
print(foods[1][2])