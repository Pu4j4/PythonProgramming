# map(): applies a function to each item in an iterable(list,tuple,etc)

# map(function, iterable)

numbers = [1,2,3,4,5,6]
multiply = map(lambda x:x*2,numbers)
print(list(multiply))

store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]
# to_euros = lambda euro: (euro[0],euro[1]*0.82)
# store_euros = list(map(to_euros, store))
# print(store_euros)
# for i in store_euros:
#     print(i)

to_dollars = lambda dollar:  (dollar[0],dollar[1]/0.82)
store_dollars =list(map(to_dollars,store))
for i in store_dollars:
    print(i)

