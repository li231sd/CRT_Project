import random

word_bank = ["python", "java",  "rocket", "banana", "castle", "guitar", "penguin", "volcano", "diamond",
    "backpack", "shampoo", "library", "wizard", "pillow", "sunflower",
    "notebook", "crocodile", "hurricane", "marble", "tractor", "jungle",
    "cupcake", "kangaroo", "blanket", "satellite", "firework", "pumpkin",
    "wallet", "dolphin", "broccoli", "airplane", "treasure", "octopus",
    "football", "telescope", "cactus", "pyramid", "whistle", "mountain",
    "bicycle", "cookie", "butterfly", "lighthouse", "elephant", "parrot",
    "scissors", "watermelon", "snowflake", "calendar", "necklace", "monitor",
    "keyboard", "sandwich", "headphones", "chocolate", "spaceship", "squirrel",
    "hamburger", "pineapple", "festival", "umbrella", "tornado", "rainbow",
    "jacket", "penguin", "violin", "restaurant", "dragon", "battery",
    "microscope", "vacation", "magnet", "feather", "engine", "compass",
    "baseball", "hospital", "lantern", "skateboard", "meadow", "sunrise",
    "popcorn", "pencil", "wallet", "bridge", "cannon", "ocean", "window",
    "printer", "gorilla", "sapphire", "peacock", "museum", "fireplace",
    "volleyball", "garden", "camera", "toothbrush", "refrigerator",
    "mosquito", "caterpillar", "beehive", "adventure", "astronaut", "pirate",
    "snowman", "helmet", "drizzle", "submarine", "glacier", "barn",
    "dinosaur", "mailbox", "jellyfish", "blueberry", "parachute", "campfire",
    "raincoat", "avocado", "bracelet", "tiger", "zebra", "coconut",
    "orchestra", "planet", "asteroid", "meteor", "galaxy", "nebula",
    "cabin", "orchid", "phoenix", "trellis", "quartz", "walrus",
    "buffalo", "chimney", "cushion", "anchor", "canyon", "hedgehog",
    "mushroom", "pretzel", "sailboat", "thunder", "whirlpool", "yogurt",
    "zeppelin", "goblin", "griffin", "emerald", "topaz", "opal",
    "ruby", "crystal", "bronze", "silver", "golden", "harvest",
    "journey", "voyage", "forest", "desert", "valley", "river",
    "waterfall", "cliff", "prairie", "island", "cavern", "geyser",
    "falcon", "raven", "hawk", "sparrow", "owl", "heron",
    "otter", "beaver", "hamster", "rabbit", "cheetah", "panther",
    "leopard", "rhino", "hippopotamus", "koala", "alpaca", "camel",
    "donkey", "llama", "goose", "turkey", "salmon", "lobster",
    "shrimp", "oyster", "coral", "seashell", "starfish", "seahorse",
    "kayak", "canoe", "paddle", "lifeguard", "surfboard", "binoculars",
    "hourglass", "windmill", "ladder", "toolbox", "workshop", "blueprint",
    "engineer", "chemist", "teacher", "student", "captain", "detective",
    "magician", "inventor", "explorer", "artist" ]

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
