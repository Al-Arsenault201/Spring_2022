# in-class coding for Monday, February 14

#  for now, just do this:

#if __name__ == "__main__":
    #everything is indented

# def main:  - this is the old way to do it; don't do this
   # a bunch of stuff

# create an empty list
grocery_list = []

# a list can have zero or more elements

#how many elements are in the list?
len(grocery_list)

#easiest way to add an element is with append

#append adds a value to the END of the list, wherever the end is.
grocery_list.append("Milk")
grocery_list.append("Eggs")
grocery_list.append(9)


# remove removes an element from the list by its value
# and it only removes the FIRST occurrence of that value
grocery_list.remove(9)

# what if you want to add an element, but not at the end?

#insert a value into the list in a specific place, not necessarily the end
grocery_list.insert(1, "Bagels")

#the value of the FIRST element in the list
grocery_list[0]  # the first element has index 0

# Python provides us the "in" operator that lets us know whether a value is in a list or not
if "Strawberries" in grocery_list:
    grocery_list.remove("Strawberries")

# a common error - getting the list index wrong
new_grocery_list = ["Milk", "Eggs", "Cereal", "Coffee", "Apples", "Strawberries", "Broccoli", "Cucumber", "Tomatoes", "Green Onions"]

#the last element in the list always has index len(list) -1
# we can call list[-1]

