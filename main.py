# This tag for comments 
# print code 
#print("Hello, World!")
# End of the code
# This is a simple Python script that prints "Hello, World!" to the console.

# Variables and Data Types in Python
#x = 5
#y = 10
#sum = x + y
#print("This sum of x = ",x, " and the y = ",y, "this is the sum =",sum)

# Variable naming conventions in Python
#myvar = "John"
#my_var = "John"
#_my_var = "John"
#myVar = "John"
#MYVAR = "John"
#myvar2 = "John"


# Multiple variable assignment
#x, y, z = "Orange", "Banana", "Cherry"
#print(x)
#print(y)
#print(z)

# One value to multiple variables
#x = y = z = "Orange"
#print(x)
#print(y)
#print(z)


# Unpack a collection
#fruits = ["apple", "banana", "cherry"]
#x, y, z = fruits
#print(x)
#print(y)
#print(z)


# Output variables

#x = 22

#def myfunc():
 #   y = 300
  #  print(x + y)

#myfunc()




# while True:
#     num = input ("enter a int or string ")

#     num2 = random.randint(1,100)
    
#     try:
#         val = int(num)
#         if val == num2:
#             print ("you win", " the random number was: ", num2)
#             break
#         else:
#             if val > num2:
#                 print ("too high")
#             elif val < num2:
#                 print ("too low")        
#         continue
#     except ValueError:
#         print ("you entered a strintg ")


import random
num2 = random.randint(1,100)
while True:
    num = input ("you have to inter a int number ")
   
    try:
        val = int(num)
        if val == num2:
            print ("you win")
            break
        elif val > num2:
            print ( "too high", num2)
        elif val < num2:
            print ("too low", num2)
            continue
    except ValueError:
        print ("you have to inter a int number")




