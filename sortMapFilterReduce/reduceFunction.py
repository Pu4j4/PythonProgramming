# reduce(): apply a function to an iterable and reduce it to a single cumulative value.
# performs function on first two elements and repeats process until 1 value remains

from functools import reduce

#
# nums = [1, 2, 3, 4, 5]
# result = reduce(lambda x, y: x + y, nums, 10)
# print(result)


# letters = ["H","E","L","L","O"]
# word = reduce(lambda x,y: x + y,letters)
# print(word)

num = [2,4,6,8,10]
result = reduce(lambda x,y :x * y,num)
print(result)

# fact = [5,4,3,2,1]
# result = reduce(lambda x,y: x * y,fact)
# print(result)