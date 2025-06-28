# filter(): creates a collection of elements from an iterable for which a function returns true
# filter(function, iterable)

friends = [("bhanu",22),
           ("mike", 20),
           ("cherry", 18),
           ("navi", 16),
           ("john", 19),
           ("bob", 17)]

age = lambda data: data[1]>=18

drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i)