# indicates a comment

# a comment is NOT part of your program
# it is a note to humans about what you think you are trying to do

"""
Name: ALfred Arsenault
Date: 2/2/22
Class: CMSC 201 Section 40
Assignment: Sample code for 2/2

"""

#Literals -"exactly this"

print("Hello, World")  #print literally this - exactly

# string literal
# mark a string either by " "  or ' ' - don't mix them

print(42)  #integer literal

print(3.14159) # float literal

"""
A 'magic number' is an int or float literal that has no 
obvious explanation

"""
a = "Hello, world"  # declare and assign a variable

print(a)

#you don't have to pre-define a variable
# str a  - works in C & related languages

#but - we have to assign a value
print(b)

#the opposite of print is input
#input statement prints a prompt on the screen and waits until the user types something in

your_number = input("Please enter a number")

"""
write a program that prompts the user to enter the age of their pet
then print out a friendly message telling the user the pet's age
"""
pet_age = input("Please enter the age of your pet")
print("You said your pet's age is ")
print(pet_age)