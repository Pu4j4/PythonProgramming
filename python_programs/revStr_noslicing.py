def reverse_string(text):
    result = ""
    for i in text:
        result = i + result
    return result
print(reverse_string("bhanu"))