#Dictionary:  collection which is ordered*, changeable and do not allow duplicates
# and are used to store data values in key:value pairs.
#
my_dict = {
    "name": "bhanu",
    "age": 21,
    "profession": "student",
    "birthYear": 2002
}
# print(my_dict)
# print(my_dict["name"])
#
# x = my_dict.get("age")
# print(x)
# print(my_dict.keys())
# print(my_dict.values())
#
# my_dict["name"] = "pooja"
# print(my_dict)
#
# my_dict.update({"name": "Bhanu"})
# print(my_dict)
#
# my_dict["favfood"] = "biryani"
# print(my_dict)
#
# my_dict.pop("birthYear")
# print(my_dict)
#
# # my_dict.clear()
# # print(my_dict)
#
# print(my_dict.items())
#
# for key,value in my_dict.items():
#     print(key,value)
#
# for x in my_dict:
#     print(x)  #key names

# for x in my_dict:
#     print(my_dict[x]) #values

# for x in my_dict.values():
#     print(x)
#
# for x in my_dict.keys():
#     print(x)

# for x,y in my_dict.items():
#     print(x,y)

#Nested Dictionaries
dict1 = {
    "child1":{
        "name" : "bob",
        "year" : 2002
    },
    "child2":{
        "name" : "john",
        "year" : 2004
    }
}
print(dict1["child1"]["name"])
print(dict1["child1"]["year"])

print(dict1["child2"]["name"])
print(dict1["child2"]["year"])