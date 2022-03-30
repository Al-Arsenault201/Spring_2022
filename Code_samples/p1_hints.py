
def get_input(valid_choices):
    """
    function to make sure that we have a valid option from the user
    :return: a string that is the user's valid option
    """

    choice = input("What do you want to count on this turn?")
    while not choice in valid_choices:
        print("I'm sorry; that is not currently a valid choice, please try again")
        choice = input("What do you want to count on this turn?")
    return choice

"""
how do you tell if you have three of a kind, etc?
"""
import random
TOTAL_DICE = 5
def roll_dice():
    """
    :return: a list containing five integers representing dice rolls between 1 and 6.
    """
    roll_list = []
    for i in range(TOTAL_DICE):
        roll_list.append(random.randint(1, 6))
    return roll_list

def play_game(num_rounds):

    """
    warning: because of the order I discussed this in class, the code below WON'T work in this order.
    You'll have to rearrange the statements.

    :param num_rounds:
    :return:
    """
    num_of_each = [0,0,0,0,0,0,0]
    result = roll_dice()
    for i in range(TOTAL_DICE):
        num_of_each[result[i]] += 1
    #do I have 3 of a kind?
    if 3 in num_of_each:
        # you have 3 of a kind; score appropriately
    if 4 in num_of_each:
        # you have 4 of a kind; score appropriately
    if 5 in num_of_each:
        # you have pytzee; score appropriately
    if 3 in num_of_each and 2 in num_of_each:
        # you have a full house; score appropriately
    if num_of_each[1] == num_of_each[2] == num_of_each[3] == num_of_each[4] == num_of_each[5] == 1 or
        num_of_each[2] == num_of_each[3] == num_of_each[4] == num_of_each[5] == num_of_each[6] == 1:
        # you have a large straight; score appropriately
    # small straight is a little more awkward
    if (num_of_each[1] >= 1 and num_of_each[2]>= 1 and num_of_each[3]>= 1 and num_of_each[4] >= 1) :
        # check for 2, 3, 4, and 5
        # check for 3, 4, 5, and 6

    valid_choices = ["3 of a kind", "4 of a kind", "four of a kind",
                         "three of a kind", "chance", "small straight",
                         "large straight", "pytzee", "count 1", "count 2",
                         "count 3", "count 4", "count 5", "count 6"]
    option = get_input(valid_choices)
    if not option == "pytzee":
        valid_choices.remove(option)  # this makes sure the user only has the option of counting each type once

if __name__ == "__main__":
    num_rounds = int(input('What is the number of rounds that you want to play? '))
    seed = int(input('Enter the seed or 0 to use a random seed: '))
    if seed:
        random.seed(seed)
    play_game(num_rounds)