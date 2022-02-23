# in-class coding from Wednesday, February 23

states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado", "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]



nums = [1,2,3,4,5,6]

#print out the list, in order
print("forward")
for i in range(0, len(nums),1):
  print (nums[i])

# if you're using a negatives step, the start has to be greater than the end
print("backward")
for i in range(len(nums)-1,-1,-1):
  print(nums[i])


#print out the list of states using a while loop

i = 0  # assign an initial value
while i < len(states):  # statement - boolean is i< len(states)
  print(states[i])      #anything indented is in the loop
  print (i, len(states))  # to illustrate
  i += 1

# print out the first 100 odd integers, in reverse order
num = 199
while num != 0:
  print(num)
  num -= 2

# to fix that

num = 199
while num >= 0:
  print(num)
  num -= 2


# a loop that never gets executed

#an example of a sentinel while loop.  The letter "Q" is the sentinel.

name = input("Enter your name; enter Q to quit")  #priming read
while name != "Q":
  print(name)
  name = input("Enter your name; enter Q to quit")

# I want to add a new state to the US
# and I want to put it in my list in alphabetical order
# I'm going to use a while loop to do that

new_state = input("What is the name of the new state?")  #priming read
i = 0
while new_state > states[i]:
  i += 1
# i now holds the index of the last state that comes before new_state
states.insert(i,new_state)
print(states)


#how not to do it
grade = input("please enter your grade; enter q to quit")
for i in range(10000):
  if grade == 'q':
    break
  else:
    grade = input("please enter your grade; enter q to quit")

