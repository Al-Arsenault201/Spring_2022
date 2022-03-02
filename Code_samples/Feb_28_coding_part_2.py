# More coding from Monday, February 28

def calculate_days (years, months, days):
	num_days = 365 * years + 30 * months + days
	if years > 4:
		num_days += 1
	return num_days

if __name__ == "__main__":
    y = 23
    m = 11
    d = 6

"""
 num_days = 365 * y + 30 * m + d
    if y > 4:
        num_days += 1
"""

    answer = calculate_days(y, m, d) # y, m, d are arguments
    print(answer)

def subtract(x, y):
	print(x,"-",y,"=",str(x-y))
if __name__ == "__main__":
    x = 3
    y = 4
    subtract(y, x)


def subtract(x, y):
	print(x,"-",y,"=",str(x-y))
if __name__ == "__main__":
    x = 3
    y = 4
    subtract(y)


# new program

def factorial(x):
    if x > 0:
        product = 1
        for i in range(1,x+1):
            product *= i
        return product
    else:
        return 1

if __name__ == "__main__":
    num = int(input("Enter the number whose factorial will be calculated"))
    fact = factorial(num)
    print(num, " factorial is ", fact)

