# name = "Bhanupooja"
#
# print(name)
# print(len(name))
# print(name.lower())
# print(name.upper())
# print(name.find("a"))
# print(name.capitalize())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("o"))
# print(name.replace("o","u"))
# print(name*3)

#String Slicing
#Slicing: create a substring by extracting elements from another string
#Indexing[] or slice()
#[start:stop:step]
# name = "Bhanu pooja"
# first_name = name[0:6]
# print(first_name)
# last_name = name[6:11]
# print(last_name)
# print(first_name+last_name)
# funky_name = name[0:11:2]
# # funky_name=name[::2]
# print(funky_name)
# #reverse string
# reversed_name = name[::-1]
# print(reversed_name)

#slice()
website1 = "http://google.com"
website2 = "http://wikipedia.com"
sliced = slice(7,-4)
print(website1[sliced])
print(website2[sliced])