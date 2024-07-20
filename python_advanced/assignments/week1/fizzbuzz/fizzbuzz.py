
# Assignment:
# Write a program that automatically prints the solution to the FizzBuzz game.
# Hints:
# - Your program should print each number from 1 to 100
# - When the number is divisible by 3 then instead of printing the number, it should print "Fizz"
# - When the number is divisible by 5 then instead of printing the number, it should print "Buzz"
# - Then if the number is divisible by both 3 and 5, it should print "FizzBuzz"


# Loop through numbers from 1 to 100
for number in range(1, 101):
    # Check if the number is divisible by both 3 and 5
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")  # Print "FizzBuzz" for numbers divisible by both 3 and 5
    # Check if the number is divisible by 3
    elif number % 3 == 0:
        print("Fizz")  # Print "Fizz" for numbers divisible by 3
    # Check if the number is divisible by 5
    elif number % 5 == 0:
        print("Buzz")  # Print "Buzz" for numbers divisible by 5
    else:
        print(number)  # Print the number if it is not divisible by 3 or 5
