import random

word_bank = ["python", "java", "apple", "cherry", "date", "fig", "mouse", "phone", "notebook", "fish", "tail"]
random_word = random.choice(word_bank)

guessed_letters = []
lives = 6

# Prints out the current string
def print_current_string(guessed_letters=list[str]):
    current_string = ""
    
    for letter in random_word:
        if letter in guessed_letters:
            current_string += letter
        else:
            current_string += "_ "

    print(current_string)

def print_guessed_letters():
    print(f"Guessed letters: {guessed_letters}")

# Resets the game
def reset_game():
    global lives
    
    lives = 6

# Returns if user needs to guess again?
def exception_handling(guess): #Add user input var for parameter
    if len(guess) != 1 or not guess.isalpha():
        pass

print("Let's play hangman!")

while True:
    print_current_string(guessed_letters)
    print(f"Lives left: {lives}")
    guess = input("Guess a letter: ")   
    
    