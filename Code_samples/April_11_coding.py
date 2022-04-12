# in-class coding for Monday, April 11

#first, our recursive version of the palindrome problem

def is_palindrome(phrase):
    """
    Function recursively determines whether a string is a palindrome;
    that is the same forwards and backwards
    :param phrase: string we are checking
    :return: a Boolean; True if phrase is a palindrome and False if
    it's not
    """
    #make sure the user understands what's going on
    print("the current phrase is, ", phrase)
    input("hit enter to continue")
    #code for base cases
    if len(phrase) < 2:
        print ("phrase length", len(phrase))
        return True
    elif phrase[0] != phrase[-1]: # if the first and last characters are different it's not a palindrome
        return False

    #now write the code for the recursive
    else:
        return is_palindrome(phrase[1:-1]) #recursive call
        # strip the first and last character out
        # the answer for the string is the answer for the substring

def iterative_is_palindrome(phrase):
    """
    Iterative function to illustrate we can solve this problem that way
    :param phrase:
    :return: boolean; True if palindrome; False otherwise
    """
    palindrome = True
    while len(phrase) >= 2 and palindrome:
        if phrase[0] == phrase[-1]:
            phrase = phrase[1:-1]
        else:
            palindrome = False
    #when the loop ends, we just return the value of the Boolean palindrome
    # if it's True, this is a palindrome and if it's False it's not
    return palindrome

if __name__ == "__main__":
    word = input("enter a phrase to check if it is a palindrome")
#    answer = is_palindrome(word)
    answer = iterative_is_palindrome (word)
    print (answer)