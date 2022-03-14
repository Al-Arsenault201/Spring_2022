# here is an illustration of file I/O to solve the Wordle game
from random import randint


def get_word_list():
    """

    :return: a list of 5-letter words to be used in the program
    """
    with open("/Users/alfredarsenault/PycharmProjects/Spring_2022/sgb-words.txt","r") as infile: #gets the file ready to ready
        #read the entire file as a single string
        data = infile.read()
        word_list = data.split("\n")
        return word_list

        #read in the file one line at a time
#        new_data = []
#       for line in infile:
#           new_data.append(line)

#        this_data = infile.readlines()

def choose_answer(word_list):
    index = randint(0, len(word_list)-1)
    answer = word_list[index]
    return answer

def check_answer(guess, target):
    answer_string = ""
    for i in range(len(guess)):
        if guess[i] == target[i]:
            answer_string = answer_string + "g"
        elif guess[i] in target:
            answer_string = answer_string + "y"
        else:
            answer_string = answer_string + "_"
    print(answer_string)
    if answer_string == "ggggg":
        return True
    else:
        return False

if __name__ == "__main__":
    words = get_word_list()
    target = choose_answer(words)
    solved = False
    i = 0
    while not solved and i < 6:
        #let the user have a guess
        guess = input("What is your guess this time?")
        while not guess in words:  # this means the user has not guessed a valid 5-letter word:
            print("Error; this is not a valid 5-letter word")
            guess = input("Please enter a valid 5-letter word")
        solved = check_answer(guess, target)
        i += 1
    if solved:
        print("You won the game")
    else:
        print("Sorry, you lost. The answer was ", target, "\n better luck next time")
