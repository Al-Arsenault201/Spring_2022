# example on how to score each roll of the dice in project 1
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

def get_valid_choice(choice, num_of_each, roll):
    choice = input("What do you want to play this turn?")
    return choice

def calc_score (choice, roll):
    """
    Description: this is going to be a big honking if-elif-else
    statement that assigns the proper number of points for each roll
    :param choice: what the user chose to score
    :return: the score earned by this round
    """
    #first lets take care of count 1, count 2 count 3, count 4 count 5 and count 6
    if choice [0:5] == "count":  # this is count 1 through count 6
        c = choice.split()       # gives me a list; c[0] = "count" and c[1] is the number to count
        num = int(c[1])          # we have to cast to an int

        #go back and get my num_of_each list
        num_of_each = num_in_roll(roll)      # same call we used before
        score = num * num_of_each[num]       # the score is 3 time the number of 3's, or 4 times the number of 4's, or..
        return score
    elif choice == "3 of a kind" or choice == "three of a kind" or choice == "4 of a kind" or choice == "four of a kind":
        return sum(roll)                     # sum just adds the five dice together
    elif choice == "full house":
        return 25
    elif choice == "small straight":
        return 30


def play_game(num_rounds):
    """

    :param num_rounds: how many times the dice will be rolled
    :return:
    """
    for i in range(num_rounds):
        valid_choices = ["3 of a kind", "4 of a kind", "four of a kind",
                         "three of a kind", "chance", "small straight",
                         "large straight", "pytzee", "count 1", "count 2",
                         "count 3", "count 4", "count 5", "count 6"]
        roll = roll_dice()   # now we have the results of one roll
        print ("your roll was", roll)
        num_of_each = num_in_roll(roll)
        choice = get_valid_choice(valid_choices, num_of_each, roll)
        if not choice == "pytzee":
            valid_choices.remove(choice)  # this makes sure the user only has the option of counting each type once
    # calculate the score for this roll
        roll_score = calc_score(choice, roll)
        print("Your score on this roll was ", roll_score)



if __name__ == '__main__':
    num_rounds = int(input('What is the number of rounds that you want to play? '))
    seed = int(input('Enter the seed or 0 to use a random seed: '))
    if seed:
        random.seed(seed)
    play_game(num_rounds)
    print ("Okay we're done")