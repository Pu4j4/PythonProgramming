#1. check if a string is a palindrome
# x = input("enter a string")
# y = x[::-1]
# if x == y:
#     print(f"{x} is a palindrome")
# else:
#     print(f"{x} is not palindrome")

#2. palindrome using reversed function
# x = "malayalam"
# reversed_string = ''.join(reversed(x))
# if x == reversed_string:
#     print("yes, it is a palindrome")
# else:
#     print("No, it is not a palindrome")

#3. palindrome number
# x = 121
# y = int(str(x)[::-1])
# if x == y:
#     print("palindrome")
# else:
#     print("not palindrome")

#4. using for loop

word = "121"
rev = ""
for char in word:
    rev = char + rev
if word == rev:
    print("palindrome")
else:
    print("not palindrome")


