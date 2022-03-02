# in-class coding for Wednesday, March 2

def factorial(x):
   if x > 0:
       product = 1
       for i in range(1,x+1):
           product *= i
#       return product
       print("I am after the return")
   else:
       return 1

if __name__ == "__main__":
   num = int(input("Enter the number whose factorial will be calculated"))
   fact = factorial(num)
   print(num, " factorial is ", fact)



