
# in this file i have practice every concept of python that i have learned so far in a single file to make it easier for me to revise and also to have a better understanding of the concepts by seeing them all together in one place
# i dont know what happened to me that all the things are just compiled into one file


# print("Hello, World!")
# # This is a comment    
# #executing multiple print stsatements in a single line
# print("\nPrint Statements")
# print("mey name is dash ", end=" ")
# print("hello baidshf")
# print(" hello once agiain")
# print(" soory i keep repeating again and agin 75768 and forget my typing mistakes")
# print("\nType casting & Variables")
# x = str(5) # overwiting x and type castingint into float
# print(x)
# print(type(x))
# # we can define multiple variables at the smae time
# a, b, c =19,24.983,"dash_man"
# print(a);print(b);print(c)
# #we can also assign same values to multiple variables
# x=y=z="hammad"
# print(x);print(y);print(z)
# #unpacking an arry or a list
# names = ["baby","dash","man"]
# x,y,z=names
# print(x);print(y);print(z)
# # global variables 
# # everthing that is vreatied outside the function  are called global variables
# #like every variable that i have created earlier
# print("\ndefining functions")
# x = "awesome"

# def myfunc():
#   global x # why?? to use global variable inside function
#   x = "fantastic"
#   print("Python is " + x)

# myfunc()

# print("Python is " + x)
# print("\ndata types in python \nlists")
# #they are mutable i.e we can change them
# fruits = ["apple", "banana", "cherry"]
# print(fruits[0])
# print(fruits[-1])
# fruits[1] = "orange"
# fruits.append("kiwi")# adding an element to the end of the list
# fruits.insert(1,"mango")# adding an element at specific position
# fruits.remove("orange")# removing an element from the list
# print(fruits)
# print("\ntuples")
# # they are immutable i.e we cannot change them
# tuple1 = ("car", 100, True, 45.67)
# tuple2 = "car", "bike", "123" # without parenthesis also works(tuple packing)
# print(tuple1)
# print(tuple2)
# print("\nranges")
# for i in range(5):
#    print(i, end=" ")
# print()   
# for k in range(5,0,-1):
#    print(k, end=" ")
# # Convert a range object to a list to see its contents
# r = range(1, 5)
# print(list(r))
# print("\ndictionaries")
# user_data = {
#    "name" : "manish",
#    "age" : 25,
#    "city" : "London",
#    "hobbies": ["reading", "hiking"]
# }   
# # Accessing the value associated with the key "username"
# print(user_data["name"])
# # Using .get()
# print(user_data.get("birthplace", "Not Available"))
# # Output: Not Available

# print("\nsets")
# data_set = {"apple", "banana", "apple", 42}

# # 1. Automatic duplicate removal
# print(data_set) 
# # 2. Mutability: Adding an element
# data_set.add("cherry")
# print(data_set) 
# data_set.remove(42)
# print(data_set) 
# #creating an empty set
# set1 = ()
# #creating an empty dictionary
# dict1 = {}
# #frozen sets
# frozen_set1 = frozenset(["apple", "banana", "cherry"])
# print(frozen_set1)  
# #frozen sets are immutable i.e we cannot add or remove elements from them
# x = memoryview(bytes(5))
# print(x)
# print(type(x)) 
# # how to dosplay random numbers
# import random
# print(random.randrange(2,20))

# #multiple line strings
# multi_line_string = """This is a string that spans
# multiple lines."""

# #strings are like array you can access elements using indexing
# print(multi_line_string[0])

# #you can check whethere
# print("string" in multi_line_string)
# #slicing of strings
# b = " Hello, World! "
# print(b[2:5])
# print(b.upper())
# print(b.lower())
# print(b.strip()) # removes whitespace from the beginning and the end
# print(b.replace("H", "J"))# replaces all occurrences of "H" with "J"
# print(b.split(",")) # splits the string into a list at each comma
# #fstrings
# age = 12
# txt =f"my age is {age} years old"
# print(txt)
# price = 59
# txt = f"The price is {price:.2f} dollars"
# print(txt)
# name = input("Enter your name: ")# getting user input
# print(f"Hello, {name}!")# using fstring to greet the user
# print(9<10)
# x = "Hello"
# y = 15

# print(bool(x))
# print(bool(y))
# x = 200.08
# print(isinstance(x, int))
# import random  
# user = int(input("Enter a number between 1 and 20: "))
# x = random.randint(1, 20)
# while x!=user:
#      user = int(input("Try again! Enter a number between 1 and 20: "))
# print(f"you correctly guessed the number{x} and you number was{user}:")    
# x = input("enter the string:")
# def length_string (x):
#     count=0
#     for i in x:
#         count+=1
#     print(f"the length of the string is {count}")    
# length_string(x)    

# balance = 10000
# def menu():
#     print("enter your choice")
#     x =int(input("1.check balance\n2.withdraw money\n3.deposit money\n4.exit\n"))
#     return x
# def check_balance():
#     print(f"your balance is {balance}")
# def withdraw_money():         
#     global balance
#     amount = int(input("enter the amount to withdraw:"))
#     if amount > balance:
#          print("insufficient balance")
#     else:
#       balance -= amount
#       print(f"you have withdrawn {amount}. your new balance is {balance}")
# def deposit_money():
#     global balance
#     amount = int(input("enter the amount to deposit:"))
#     balance += amount
#     print(f"you have deposited {amount}. your new balance is {balance}")
# choice = int(0)  

# while choice !=4: 
#    choice = menu()
#    if choice == 1:
#        check_balance()
#    elif choice == 2:
#        withdraw_money()
#    elif choice == 3:
#        deposit_money()
#    elif choice == 4:
#        print("thank you for using our services")

# x = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(x)
# print(type(x))
# print(x[:4])  # Corrected line: added closing parenthesis
# print(x[2:])  # Corrected line: added closing parenthesis
# if "apple" in x:
#     print("yes, 'apple' is in the fruits list")

# thislist = ["apple", "banana", "cherry"]
# x = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(x)
# print(type(x))
# print(x[:4])  # Corrected line: added closing parenthesis
# print(x[2:])  # Corrected line: added closing parenthesis
# if "apple" in x:
#     print("yes, 'apple' is in the fruits list")

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.pop(1)#to remove the spesific item form the list
# del thislist #to delete the list completely
# # thislist.clear() # to clear the list but keep the list
# thislist.extend(tropical)
# print(thislist)         
# range(5)  # Generates 0, 1, 2, 3, 4
# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):# iterating through the list using index
#   print(thislist[i])
# newlist =[x for x in thislist if x!="apple"]
# print (newlist)
# # .upper() to converts string into all caps
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

# thislist.sort()

# print(thislist)
# thislist.sort(reverse = True)
# print(thislist)
# # you cannot remove an item in a tuple
# # len() functionis used for all kinds of arrays( lists, tuples, sets, dictionaries)
# x=input("enter item name:")
# y=int(input("enter item qty:"))
# z=int(input("enter price per item:"))
# total_price =y*z
# print(f"total cost of {y} {x} is {total_price}")
# def name_func():
#     simple_name = input("enter your name:")
#     cleared_name = simple_name.strip()
#     title_name = cleared_name.title()
#     print(title_name)
# name_func()
# print("Item price Calculator")
# a = []
# def calc():
#         name = input("ENter the name")
#         quantity = int(input("Enter the quantity"))
#         price = int(input("Enter the price"))
#         a.append([name,quantity,price])
#         print(a)
#         print(f"Total price for {a[0][0]} of {a[0][1]} is {a[0][2] * a[0][1]}")
#         print(a)

# calc()
# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()

# print(x) #before the change

# car["year"] = "1000"

# print(x) #after the change
# print(car)
# # .copy() is the commeand used to copy on so callled arryas into another variables if you want
# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }# nested dictionaries
# print(myfamily["child2"]["name"])
# for x, obj in myfamily.items():
#   print(x)

#   for y in obj:
#     print(y + ':', obj[y])#nested loop to access nested dictionaries
# a = 33
# b = 200

# if b > a:
#   pass#pass is used when you have an if statement and you wnat to do nothing
##match statements
# day = 4
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalid day")# default case symbol '_'

# # you can also check more than 1 statements in a case statement like"1|2|3|4:"
# # you can use if staements as an exra guard like case 4 if day <5:
# # while loop
# i=1
# while i<=10:
#     print(f"{i} ",end="")
#     i+=1
# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")
# #this else statement could also be used in for loops
# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:#nested for loops
#     print(x, y)    
# def my_function(name = "friend"):# you can assgn defualt values to a function parameter
#   print("Hello", name)

# my_function("Emil")
# my_function("Tobias")
# my_function()
# my_function("Linus")
# def my_function(animal, name):# you can give a fuction its vlaue in the form of key value pairs
#   print("I have a", animal)
#   print("My", animal + "'s name is", name)

# my_function(animal = "dog", name = "Buddy")
# my_function("buddy","dog")# when oyu provide the arguments with out key  this is called potionsl arguments
# def my_function(*kids):# if you dont know how many arguments are to be passed you can use * before the argument
#   print("The youngest child is " + kids[2])# * args is used with argumentts
#   #**kwargs is used with key workd args
# my_function("Emil", "Tobias", "Linus")
# #decorators
# def my_decorator(func):
#   def wrapper():
#     print("Something is happening before the function is called.")
#     func()
#     print("Something is happening after the function is called.")
#   return wrapper
# @my_decorator
# def say_hello():
#   print("Hello!")
# say_hello()
#lambda arguments : expression

# x = lambda a : a + 10
# print(x(5))
# x = [7,6,5,4,3,2,1]
# for i in range(len(x)):
#     for i in x:
#         print(i)
#     x.pop(0)   
# mystr = "banana"
# myit = iter(mystr)

# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# import mymodule
# mymodule.greeting("ht")    
# import datetime
# x = datetime.datetime.now()
# print(x)

# print(x.year)
# print(x.strftime("%A"))
# import re
# x = input("enter the logical expression:")
# y=re.sub(r" && "," and ", x)
# z=re.sub(r" \|\| "," or ", y)
# print(z)
# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     arr.sort(key=None, reverse=True)
#     print(arr)
# list2 = []
# scores = []
# for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         list1 = [name,score]
#         list2.append(list1)
  
# for student in list2:
#     scores.append(student[1])
# lowest=scores[0]
# for x in scores:
#     if (lowest>x):
#        lowest = x
# second_lowest=float('inf')  
# name =[]   
# for x in scores:
#     if (lowest<x and x<second_lowest):
#         second_lowest = x
# for student in list2:
#     if student[1]==second_lowest:
#         name.append(student[0])
# name.sort()
# for name in name:
#     print(name)
# file = open("demofile.txt", "a")
# file.write("Jinay mera dil lutya ohoh \nJinay menu mar stya ohoh\n")
# # file.close()
# file = open("demofile.txt", "r")
# print(file.read())
# file = open("demofile.txt", "r")
# for line in file:
#     print(line)

# file.close()
import sys
print(sys.version)
import numpy as np
import pandas as pd
print(np.__version__)
print(pd.__version__)