# the recursive version of the "sum a list of integers" problem
def sum_numbers(nums):
    """
    Recursive function that sums a list of numbers
    :param nums: list of numbers of which we will find the sum
    :return: integer or float that is the sum of the list
    """
    #base case first
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        print ("only one list item")
        return nums[0]
    else:
        a = nums[0] + sum_numbers(nums[1:])
        print("current number is ", nums[0], "current sum = ", a)
        return a




if __name__ == "__main__":
    numbers = [1,2,3,4,5]
    answer = sum_numbers(numbers)
    print(answer)