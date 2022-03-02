# an example of scope in Python
DIGITS = ['0','1','2','3','4','5','6','7','8','9']

def get_input():
    """

    :return:
    """
    #This is a nested funct. error_check is contained WITHIN get_input and it
    # can ONLY be called by get_input

    def error_check(s):
        """
        This is a helper function that determines whether the user typed in a
        positive integer or not
        :param s: the string the user typed
        :return: Boolean; True if this is a positive integer; false otherwise
        """
        is_number = True
        for char in s:
            if not char in DIGITS:
                is_number = False
        return is_number

    num = input("Enter a positive integer; we will calculate that number's factorial")
    is_num = error_check(num)
    while not is_num:
        print("Error; that is not a positive integer")
        num = input("Enter a positive integer; we will calculate that number's factorial")
        is_num = error_check(num)
    # now we know that num is a positive integer and we can cast it
    num = int(num)
    return num

def factorial(n):
    product = 1
    for i in range(1,n+1):
        product *= i
    return product

def print_answer(n, fact):
    print(n, "factorial is ", fact)

# now the main program
if __name__ == "__main__":
    num = get_input()
    answer = factorial(num)
    print_answer(num, answer)
