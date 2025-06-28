#counting vowels in a string

text = input("enter a string: ").lower()
vowels = "aeiou"
count = 0
for i in text:
    if i in vowels:
       count += 1
print("number of vowels:",count)

#using comprehension
text = input()

