import random

word_bank = ["python", "java", "apple", "cherry", "date", "fig", "mouse", "phone", "notebook", "fish", "tail", "football", "baseball", "soccer", "tennis",
    "badminton", "cricket", "hockey", "swimming", "running", "cycling",
    "mountain", "river", "ocean", "forest", "desert", "island", "valley",
    "volcano", "waterfall", "glacier", "rainbow", "thunder", "sunshine",
    "family", "friend", "brother", "sister", "mother", "father", "cousin",
    "holiday", "birthday", "vacation", "adventure", "journey",
    "elephant", "giraffe", "kangaroo", "dolphin", "penguin", "tiger", "lion",
    "cheetah", "monkey", "rabbit", "hamster", "squirrel", "butterfly",
    "airplane", "bicycle", "motorcycle", "submarine", "helicopter", "rocket",
    "bridge", "castle", "library", "hospital", "restaurant", "airport",
    "coffee", "chocolate", "sandwich", "pancake", "spaghetti", "hamburger",
    "ice cream", "popcorn", "cookie", "breakfast", "dinner", "vegetable",
    "diamond", "emerald", "crystal", "treasure", "pirate", "wizard",
    "dragon", "knight", "castle", "adventure", "mystery", "treasure",
    "galaxy", "planet", "comet", "asteroid", "satellite", "telescope",
    "astronaut", "gravity", "universe", "nebula"]

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
    global random_word, guessed_letters, lives
    random_word = random.choice(word_bank)
    lives = 6

# Returns if user needs to guess again
def exception_handling(guess): # Add user input var for parameter
    if len(guess) != 1 or not guess.isalpha():
        return "Please enter a single letter"
    elif guess in guessed_letters:
        return "You have already guessed that letter"
    else:
        return "good"

print("Let's play hangman!")

while True:
    print_current_string(guessed_letters)
    print(f"Lives left: {lives}")
    guess = input("Guess a letter: ").lower()

    if exception_handling(guess) == "good":
        guessed_letters.append(guess)

        if guess not in random_word:
            print(f"Sorry, {guess} not in random word")
            lives -= 1

        all_letters_guessed = True

        for letter in random_word:
            if letter not in guessed_letters:
                all_letters_guessed = False
        
        if all_letters_guessed:
            print(f"Congrats! YOU WIN!")

            play_again = input("Play Again (y/n): ").lower()

            if play_again == "y":
                reset_game()
            else:
                break
        
        if lives == 0:
            print(f"Game over! The word was {random_word}")
            play_again = input("Play Again (y/n): ").lower()
            if play_again == "y":
                reset_game()
            else:
                break
