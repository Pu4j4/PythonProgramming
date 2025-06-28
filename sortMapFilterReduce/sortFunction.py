# sort() method: used with lists
# sort() function: used with iterables

# students = ["bhanu","mike","cherry","navi","kiran"]
# students.sort() #sort method
# students.sort(reverse=True)
# for i in students:
#     print(i)

# sorted_students = sorted(students)
# sorted_students = sorted(students,reverse=True)
# for i in sorted_students:
#     print(i)


students = [("bhanu", "A",98),
            ("mike", "C",75),
            ("cherry", "D",50),
            ("kiran", "F",30),
            ("navi", "B",86)]
# grade = lambda grades:grades[1]
# students.sort(key=grade)

marks = lambda mark:mark[2]
students.sort(key=marks)

# students.sort()
for i in students:
    print(i)