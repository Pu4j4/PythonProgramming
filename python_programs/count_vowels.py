#counting vowels in a string

# text = input("enter a string: ").lower()
# vowels = "aeiou"
# count = 0
# for i in text:
#     if i in vowels:
#        count += 1
# print("number of vowels:",count)

#using function
def count_vowels(text):
    vowels = "aeiou"
    return sum(1 for i in text if i in vowels)
print(count_vowels("bhanu"))

