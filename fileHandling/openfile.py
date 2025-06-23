# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.
# There are four different methods (modes) for opening a file:
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# with open("test") as file:
#     print(file.read())
# print(file.closed)

# to handle the errors with files
# try:
#     with open("test") as file:
#      print(file.read())
# except FileNotFoundError:
#     print("That file was not found :(")


f = open("written")
print(f.readline())
print(f.readline())
f.close()
