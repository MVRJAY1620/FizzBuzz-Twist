#Welcome to FizzBuzz with a Twist!
# This game is a variation of the classic FizzBuzz game.
# It includes additional rules for numbers containing '3' or '7'.
print("Welcome to FizzBuzz with a Twist!")
# Function to determine the output based on the rules of FizzBuzz with a Twist
# The rules are:
# - If the number is only divisible by 3, print "Fizz"
# - If the number is only divisible by 7, print "Buzz"   
# - If the number is divisible by both 3 and 7, print "FizzBuzz"
# - If the number contains '3' but is not divisible by 3 or 7, print "Almost Fizz"
# - If the number contains '7' but is not divisible by 3 or 7, print "Almost Buzz"      
# - Otherwise, print the number itself
def fizzbuzz(number):
    if number % 3 == 0 and number % 7 == 0:
        return "FizzBuzz"
    elif number % 3 == 0 and number % 7 != 0:
        return "Fizz"
    elif number % 7 == 0 and number % 3 != 0:
        return "Buzz"
    elif "3" in str(number):
        if number % 3 != 0 or number % 7 != 0:
            return "Almost Fizz"
    elif "7" in str(number):
        if number % 3 != 0 or number % 7 != 0:
            return "Almost Buzz"
    else:
        return str(number)
# The game will prompt the user to enter a number
number = int(input("Enter a number: "))
# The function will be called with the input number and the result will be printed
result = fizzbuzz(number)
print(f"Output of FizzBuzz with a Twist for {number}: {result}")
# The game can also be played for a range of numbers
print(f"Playing FizzBuzz with a Twist for numbers 1 to {number}:")
for i in range(1, number + 1):
    print(fizzbuzz(i))