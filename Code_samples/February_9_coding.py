# in-class coding from Wednesday, February 9

# prompt the user for a month and day, and calculate
# the julian date of that day

print ("This program prompts you to enter a month and day and prints out the julian date of that day")
month = input("Please enter a month")
day = int(input("Please enter the day of the month"))
if month == "January":
    j_date = day
elif month == "February":
    j_date = 31 + day
elif month == "March":
    j_date = 59 + day
elif month == "April":
    j_date = 90 + day
elif month == "May":
    j_date = 120 + day
elif month == "June":
    j_date = 151 + day
elif month == "July":
    j_date = 181 + day
elif month == "August":
    j_date = 212 + day
elif month == "September":
    j_date = 243 + day
elif month == "October":
    j_date = 273 + day
elif month == "November":
    j_date = 304 + day
elif month == "December":
    j_date = 334 + day
else:
    j_date = 0

if j_date == 0:
    print("I'm sorry, that's not a month I recognize")
else:
    print(month, day, "has a julian date of", j_date)

message = "This is the secret"
x = "this is the secret"

# check to see if the strings are equal
message == x

# logical operators - and, or, not
# input is boolean
# result is boolean

#not - produces the negation of its input - True becomes False; False becomes True
age = 16
age > 18
not age<= 18

#and takes TWO boolean conditions; returns True if BOTH are True; False otherwise
x = True
b = False
x and b

age = int(input("Enter an age"))
if age > 18 and age < 21:
    print("Almost there")

month = input("enter a month")
day = int(input("enter the day of the month"))
#makes a check
if month == "January" and day >= 1 and day <= 31:
    print("valid date")
elif month ==  "February" and day >= 1 and day <= 28:
    print("valid date")
else:
    print("invalid input")

# or takes TWO booleans and returns True if one or both of them is True
# or returns False ONLY if both booleans are False

day = int(input("Please enter the day in February"))
if day < 1 or day > 28:
    print("Error, invalid date")
else:
    print("okay, got it")