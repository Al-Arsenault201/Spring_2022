# in-class coding from Monday, April 4
# more discussion of/hints on Project 1

"""
    Pytzee Starter Code - Modify this with your own header here.

"""

import random

TOTAL_DICE = 5
DICE_FACES = 6
"""
    REMOVE THIS COMMENT:
        Your constants should go here.  
"""


def roll_dice():
    """
    :return: a list containing five integers representing dice rolls between 1 and 6.
    """
    roll_list = []
    for i in range(TOTAL_DICE):
        roll_list.append(random.randint(1, 6))
    return roll_list


"""
    REMOVE THIS COMMENT:
        Your additional functions should go here.  
"""

def num_in_roll(roll):
    num_of_each = [0,0,0,0,0,0,0]
    for i in range(len(roll)):
        num_of_each[roll[i]] += 1
    return num_of_each

def verify_choice(choice, num_of_each):
    if choice == "3 of a a kind":
        return 3 in num_of_each     # 3 of a kind is only valid if there is a 3 in the list num_of_each
    elif choice == "4 of a kind":
        return 4 in num_of_each
    elif choice == "full house":
        return 3 in num_of_each and 2 in num_of_each
    """
    and so on for each choice
    """


def get_valid_choice(available_choices, num_of_each):
        """
        function to make sure that we have a valid option from the user
        :return: a string that is the user's valid option
        """
# note: this doesn't completely work; we're going to change this
# during lecture
        choice = input("What do you want to count on this turn?")
        while not choice in available_choices:
            print("I'm sorry; that is not currently a valid choice, please try again")
            choice = input("What do you want to count on this turn?")
        #verify that the user really has the choice - if the user says pytzee, the user really has that.
        if not verify_choice(choice, num_of_each):
            # tell the uer this isn't valid; ask for another option
        return choice

def play_game(num_rounds):
    """

    :param num_rounds: how many times the dice will be rolled
    :return:
    """
    valid_choices = ["3 of a kind", "4 of a kind", "four of a kind",
                     "three of a kind", "chance", "small straight",
                     "large straight", "pytzee", "count 1", "count 2",
                     "count 3", "count 4", "count 5", "count 6"]
    for i in range(num_rounds):
        roll = roll_dice()   # now we have the results of one roll
        print(roll)
        num_of_each = num_in_roll(roll)
        print(num_of_each)
        choice = get_valid_choice(valid_choices, num_of_each)
        if not choice == "pytzee":
            valid_choices.remove(choice)  # this makes sure the user only has the option of counting each type once
        print (choice)

if __name__ == '__main__':
    num_rounds = int(input('What is the number of rounds that you want to play? '))
    seed = int(input('Enter the seed or 0 to use a random seed: '))
    if seed:
        random.seed(seed)
    play_game(num_rounds)
