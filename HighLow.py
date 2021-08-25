# Hi Lo game will be useful to count the number of guesses. We know that the computer should be able to get
# the correct answer

low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press Enter to start")

guesses = 1
while True:
        print("\tGuessing in the range of {} to {}".format(low, high))
        guess = low + (high - low) // 2
        high_low = input("My guess is {}. Should I guess higher or lower? "
                         "Enter h or l, or c if my guess was correct"
                          .format(guess)).casefold()

        if high_low == "h":
                # Guess higher. The low end of the range becomes 1 greater than the guess.
                low = guess + 1
        elif high_low == "l":
                # Guess lower. The high end of the range becomes one less than the guess.
                high = guess - 1
        elif high_low == "c":
                print("I got it in {} guesses!".format(guesses))
                break
        else:
                print("Please enter h, l or c")
        
        guesses = guesses + 1

# A simple typing error could result in the program never guessing correctly, and we may not detect that unless we choose a number that causes a problem
# An augment assignment is a shorthand way of assigning values to a variable
