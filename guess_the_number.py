import random


# Ask user the range to play with
game_range = int(input("What is the range you want to play with? "))

# Select a random number between the desired interval
number = random.randint(0,game_range)
guess = None

# Until the user guesses the number
while guess != number:
    try:
        
        # Ask user to guess the number
        guess = int(input(f"Please enter a number between 0 and {game_range} "))
        
        # Check if the number guessed is within the range defined
        if 0 <= guess <= game_range:
            
            # Check if the user guessed the correct number
            if guess == number:
                print(f"Congratulations! You've guessed the number was {number}")
            
            # If the user has guessed a higher number
            elif guess > number:
                print(f"{guess} is higher than the number")
                raise ValueError
            
            # If the user has guessed a lower number
            else:
                print(f"{guess} is lower than the number")
                raise ValueError
        
        # If the user has guessed a number out of range, raise a different kind of error
        else:
            raise KeyError

    # Handle the exceptions, with a proper message
    except KeyError:
        print("You should enter a number within the range.")
    except ValueError:
        print("Keep trying!")
