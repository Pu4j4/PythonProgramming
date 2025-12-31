#List comprehension: it offers a shorter syntax when you want
# to create a new list based on values of an existing list
# list = [expression for item in iterable]
# list = [expression for item in iterable if conditional]
# list = [expression if/else for item in iterable]

# squares = []
# for i in range(1,11):
#     squares.append(i*i)
# print(squares)

#the above code is equals to
# squares = [i**2 for i in range(1,11)]
# print(squares)


# nums = [1,2,3,4,5,6,7,8,9]
# for num in nums:
#     if num%2==0:
#         print(num)
#this code equals to

# even = [num for num in nums if num%2==0 ]
# print(even)

# odd = [num for num in nums if num%2!=0]
# print(odd)
#
# students = [100,90,80,70,60,50,40,30,0]
# passed_students = list(filter(lambda x: x >= 60, students))
# print(passed_students)
# #this code equals to
# passed_students = [i for i in students if i>=60]
# # passed_students = [i if i>=60 else "failed" for i in students ]
# print(passed_students)