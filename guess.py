import random

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        attempts += 1
        guess = input(f"\nAttempt {attempts}/{max_attempts}. Enter your guess: ")
        
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number!")
            attempts -= 1  # Don't count invalid attempts
            continue
        
        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"\nCongratulations! You guessed the number in {attempts} attempts!")
            break
    
    if attempts >= max_attempts and guess != secret_number:
        print(f"\nGame over! You've used all {max_attempts} attempts.")
        print(f"The secret number was {secret_number}.")

# Start the game
guess_the_number()