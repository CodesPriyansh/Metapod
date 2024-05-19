import random 

def easy():
    print("Welcome to GUESS THE NUMBER.")
    print("i'm thinking of a number between 1 to 10, can you guess it?")

    user_guess = 0
    guesses = 0
    random_number = random.randrange(11)
    while user_guess != random_number:
        user_guess = int(input("enter your guess:"))
        if user_guess < random_number:
            print("Too low! Try Again.")
        elif user_guess > random_number:
            print("Too High! Try Again.")
        else:
            print(f"Congratulations! You guessed the number {random_number} correctly in {guesses} guesses.")
            break
        guesses += 1
        
def medium():
    print("Welcome to GUESS THE NUMBER.")
    print("i'm thinking of a number between 1 to 50, can you guess it?")

    user_guess = 0
    guesses = 0
    random_number = random.randrange(51)
    while user_guess != random_number:
        user_guess = int(input("enter your guess:"))
        if user_guess < random_number:
            print("Too low! Try Again.")
        elif user_guess > random_number:
            print("Too High! Try Again.")
        else:
            print(f"Congratulations! You guessed the number {random_number} correctly in {guesses} guesses.")
            break
        guesses += 1
        
def hard():
    print("Welcome to GUESS THE NUMBER.")
    print("i'm thinking of a number between 1 to 100, can you guess it?")

    user_guess = 0
    guesses = 0
    random_number = random.randrange(101)
    while user_guess != random_number:
        user_guess = int(input("enter your guess:"))
        if user_guess < random_number:
            print("Too low! Try Again.")
        elif user_guess > random_number:
            print("Too High! Try Again.")
        else:
            print(f"Congratulations! You guessed the number {random_number} correctly in {guesses} guesses.")
            break
        guesses += 1
        
def main():
    print("which level you want to play?")
    level = input("easy, medium or hard: \n") 
    if level == "easy":
        easy() 
    elif level == "medium":
        medium() 
    else:
        hard() 
        
if __name__ == '__main__':
    main() 
    

        
        
    
        