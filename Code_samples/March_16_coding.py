# in-class coding for Wednesday, March 16

the_grid = [
    ['O','O','X','X','O'],
    ['O','O','O','X','O'],
    ['X','X','O','X','X'],
    ['O','O','O','X','O'],
    ['O','X','O','X','O']

]
# 2D list - a list whose elements are all list
# terminology: rows and columns

"""
terminology:
 refer to an individual element: the_grid[row_number][column_number]
"""

#let's check for four x's in a row - horizontal
answer = False
i = 0
while i < len(the_grid) and not answer:
    #for row i
    for j in range(len(the_grid[i])-3):
        if the_grid[i][j] == "X" and the_grid[i][j+1] == "X" and the_grid[i][j+2]=='X' and the_grid[i][j+3] == "X":
            answer = True
    i += 1

# now check to see if there are four consecutive X's in a column

col_number = 0
while col_number < len(the_grid[0]) and not answer:
    #for a specific column - check four consecutive rows
    for row_number in range(len(the_grid)-3):
        if the_grid([row_number][col_number])=='X' and the_grid[row_number+1][col_number]=='X' and the_grid[row_number + 2][col_number] == 'X' and the_grid[row_number +3][col_number]=='X':
                answer = True
    col_number += 1


# I want to populate my 2D list based on user input
# for HW5, problem 3- that's from the user at the keyboard

# create a new, blank, 2D list

alt_grid = []
# ask the user how many rows
num_rows = int(input("How many rows is your game board?"))

for i in range(num_rows):

    # I'm going to read in num_rows rows of data, one data at a time
    next_line = input("")
#    next_line = next_line.split() #depends on how the user types the input
    #if the user does not put blank spaces
    line = [] #create a new 1-d list
    #append one character at a time as a list element to line
    for letter in next_line:
        line.append(letter)
    alt_grid.append(line)


def connect_four(the_grid, player_symbol):

    """
    This is the stuff with the two different while loops that check for horizontal wins
    and vertical wins

    :param the_grid:
    :param player_symbol:
    :return:
    """

def get_input():
    """
    This is the part where you prompt for the number of rows
    read in that many rows in a loop, change each row into a one-D list
    and append that to your 2D-list
    :return:
    """

if __name__ == "__main__":
    player_symbol = "X"
    grid = get_input()
    answer = connect_four(grid,player_symbol)
    print(answer)
