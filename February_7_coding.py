# in-class coding from Monday, February 7

# first the input statement

gpa = input ("Please enter your gpa")
#the prompt must be a single string

#the input is always a string - not an int, not a float, not a boolean

# cast - tell Python to change the type
gpa = float(input("Please enter your gpa"))

div_2 = gpa/2
print(div_2)

age = int(input("enter your age in years"))
print (age + 5)

#output - you use the print command
# you can print any type we've covered - you can print strings, ints, floats, booleans

# strings - python always takes as many spaces as are in the string to be printed
message = "happy birthday"
print(message)
message2 = "we won"
print(message2)

#integer
age = 23
print(age)
answer = 423
print(answer)

#floats
x = 1.234000
print(x)
y = 1/3
print(y)

#printing multiple things
# you can print multiple values in the same print statement - separate using commas

grade = "Senior"
gpa = 4.32
print("Your grade is", grade, " and your gpa is ", gpa)

# If you have two strings, + concatenates them and creates a single string with no spaces
# in between
print("Your grade is"+"your gpa is")

# by default, Python prints a newline at the end of the print statement

print("This is the first statement")
print("This is the second statement")

# you can change that with the "end" clause

print("This is the first statement", end = "not a newline")
print("This is the second statement")

# single statement; multiple lines of output

# "\n" represents a newline character
print("First statement","\n","Second statement")

NEWLINE = "\n"
print("First statement"+NEWLINE+"Second statement")

# if you're under 18 you can't vote
# if you're 18 or older but under 21 you can vote but you can't drink alcohol
# if you're 21 or older you can both vote and drink

# "pseudocode" - English description of what you want to do
# you write Python code to implement

age = int(input("Please enter your age in years"))
if (age < 18):
    print("You can neither vote nor drink")
    print("Here's another line")
    print("and another")
elif (age < 21):
    print("you can vote but you can't drink")
else:
    print("congratulations you are officially an adult")
#this is AFTER the conditional; it is not part of it
print("the conditional is over")

# There does not have to be an elif
# there does not have to be an else

gpa = float(input("What is your gpa?"))
if gpa > 3.75:
    print("You're on the President's list")
print("the conditional is done")