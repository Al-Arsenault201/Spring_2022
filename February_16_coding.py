# in class coding for Wednesday, February 16

groceries = ["Milk","Sugar","Eggs", "Grapes","Lettuce"]

# I bought Lettuce, I can remove it from the list
groceries.remove("Lettuce")

# to get rid of the first item in the list
groceries.pop(0)

# to get rid of multiple values
del groceries[0:3]

#del is used when you want to get rid of multiple values at a time
# can you add multiple values at a time?
# no not easily

groceries.append("Broccoli","Cauliflower")

# list of states

states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado", "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

# the first ten states
first_ten = states[0:10]

# the 21st through 30th states
third_ten = states[20:30]

#split California into six states
states.remove("California")
states.append("North California")
states.append("Southern California")
states.append("Sierras")
states.append("Central California")
states.append("Old California")
states.append("Golden Gate/Silicon Valley")

# two tricks with slicing: you don't need to put a number before or after the colon

# if no number before colon, start at the beginning
print(states[:10])

# if you leave out the number after the colon, it goes until the end
print(states[50:])

school_name ="University of Maryland Baltimore County"
len(school_name)

#we can access the value of any character in a string
school_name[0]

# I can slice a string
print(school_name[11:18])

#substring is a slice of a string
last_five = school_name[-5:]

#NOTICE: nothin here has changed the original string - because you can't do that!!

# you can only reassign a string
new_school = school_name[0:3] + "!" + school_name[4:]

#to split a sentence into a list of individual words
words = school_name.split()

#default is to split on white space
# but you can specify anything

words = school_name.split("e")

#strip - get rid of leading and/or trailing white space
score = input("What was the score of the game")
print(score)

neat = score.strip()

# strip gets rid of leading and trailing white space
# if you just want to get rid of leading white space use lstrip()
# if you just want to get rid of trailing white space use rstrip()



