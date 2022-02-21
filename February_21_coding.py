# in-class coding from Monday, February 21

grocery_list = ["Milk", "Eggs", "Grapes", "apples", "chips", "fish", "dog treats"]

#print the items in the list, one item per line, so I can send someone
# to the store for me

# perfect for a "for each" loop

for item in grocery_list:
    print(item)

# solving this problem using a "for i" loop:
for i in range(0,len(grocery_list),1):
    print(grocery_list[i])

# in range:
#   the first value - 0 - is where you start
# the second value - len(grocery_list) - is where you stop - DO NOT EXECUTE
# with this value
# the third value is the hop count - how much you increment the index variable
# by each time

# you can leave out the first and the third value in the range statement
# if there are two values, the hop count defaults to 1
# if there is only one value, the start element defaults to 0


# sometimes you want to change the list inside a loop
ints = [1,2,3,4,5,6]

for number in ints:
    number += 1
print("For Each loop")
print (ints)

for i in range(len(ints)):
    ints[i] += 1
print("For I loop")
print (ints)

# lists with elements of different types
bio_data = ["Alfred","Arsenault",42,5.6,True,"Active"]

# print all this in a for each loop:
for element in bio_data:
    print(element)

word = "supercalifragilisticexpialidocious"
for i in word:
    print(i)

# go through the string character by character
# if the character is a vowel, print "Found a vowel"
# otherwise print the character

VOWELS = ['a','e','i','o','u']
for letter in word:
    if letter in VOWELS:
        print("found a vowel")
    else:
        print(letter)

# error checking on input
digits = ['0','1','2','3','4','5','6','7','8','9']

score = input("Please enter your test score")
is_digits = True
if not score[0] == '-' and not score[0] in digits:
    is_digits = False
else:
    for j in score:
        if not j in digits:
            is_digits = False

if is_digits == True:
   print ("hooray, you entered a digit")
   score = int(score)
else:
   print ("I'm sorry, that's not a valid test score")


# I will fix this online and talk about it on Wednesday

states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado", "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

# print out every state that ends in "a", one state per line
for state in states:
    if state[-1] == 'a':
        print(state)

# for i loop:

for i in range(len(states)):
    state = states[i]
    if state[-1] == 'a':
        print(state)

VOWELS = ['a','e','i','o','u','y']
for state in states:
    if state[-1] in VOWELS:
        print(state)

# harder way
for state in states:
    if state[-1] =='a' or state[-1]=='e' or state[-1] == "i" or state [-1] == 'o' or state[-1] =="u" or state[-1]=='y':
        print(state)