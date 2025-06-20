# while loop: a statement which executes the block of code as long as the specific condition is true

# count = 0
# while count<3:
#     print("hello python")
#     print(count)
#     count+=1
#
# name = ""
# while len(name)==0:
#     name =input("enter your name:")
# print("hello "+name)

#For loop: A for loop is used for iterating over a sequence, executes the block of code a limited amount of times
# for i in range(1,11):
#     print(i)
#
# for i in range(2,100,2):
#      print(i)

# for i in "python":
#     print(i)

# import time
#
# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)
# print("Happy New year")

#nested loops: a loop inside another loop, the inner loop finishes all its iterations before
# finishing one iteration of the outer loop

# rows = int(input("enter rows?"))
# columns = int(input("enter columns?"))
# # symbol = input("enter a symbol to use: ")
# for i in range(rows):
#     for j in range(columns):
#         print(i,j)
        # print(symbol, end="")
    # print()


#loop control statements(break, continue, pass)
# #break: With the break statement we can stop the loop even if the while condition is true
# x = 0
# while x < 5:
#     print(x)
#     if x == 4:
#         break
#     x+=1
#
# while True:
#     name = input("enter your name:")
#     if name!="":
#         break

# #Continue: With the continue statement we can stop the current iteration, and continue with the next
# i = 0
# while i < 10:
#     i+=1
#     if i==5:
#         continue
#     print(i)
#
# phone="123-456-789"
# for i in phone:
#     if i == "-":
#         continue
#     print(i,end="")

#pass: does nothing, acts as a placeholder
# for i in range(1,21):
#     if i==13:
#         pass
#     print(i)



# #Else: With the else statement we can run a block of code once when the condition no longer is true
# y = 1
# while y<8:
#     print(y)
#     y+=1
# else:
#     print("y is no longer less then 8")