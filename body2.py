def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Input the number for which you want to calculate the factorial
number = int(input("Enter number 1: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("The factorial of 0 is 1.")
else:
    result = factorial(number)
    print(f"The factorial of {number} is {result}")
