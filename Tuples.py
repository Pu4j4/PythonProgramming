#Tuple: collection which are ordered, immutable or unchangeable, and allow duplicate values.

my_tuple = ("apple", "banana","cherry","apple","kiwi")
print(my_tuple)
print(len(my_tuple))

print(my_tuple[1])
print(my_tuple[-1])
print(my_tuple[2:5])

#to update the values convert tuple to list
x = list(my_tuple)
x[2] = "cherries"
y = tuple(x)
print(x)

for x in my_tuple:
    print(x)

i = 0
while i<len(my_tuple):
    print(my_tuple[i])
    i+=1

tuple1 = ("pizza", True, 12, 15.23)
print(tuple1)

tuples = my_tuple + tuple1
print(tuples)

print(tuple1.count(12))
print(tuple1.index("pizza"))

if "pizza" in tuples:
    print("yes it is")

