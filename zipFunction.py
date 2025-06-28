# zip(*iterables): aggregate(collected) elements from two or more iterables(list, tuples,sets, etc)
# creates a zip object with paired elements stored in tuples for each element


# usernames = ["bhanu","mike","cherry"]
# passwords = ["Bhanu123","abc@123","guest"]
# # users = zip(usernames,passwords)
# # users = list(zip(usernames, passwords))
# users = dict(zip(usernames, passwords))
# print(type(users))
# for key,value in users.items():
#     print(key+" :  "+value)
# # for i in users:
# #     print(i)


usernames = ["bhanu","mike","cherry"]
passwords = ["Bhanu123","abc@123","guest"]
login_dates = ["1/1/2025","12/5/2025","5/11/2025"]
users = list(zip(usernames, passwords, login_dates))
for i in users:
    print(i)