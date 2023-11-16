import random

with open('SOWpods.txt', 'r') as f:
    lines = f.readlines() 
    words = [word for line in lines for word in line.split()]
    random_word = random.choice(words)  

print("Welcome to Hangman!")

word = (random_word)  
guessed_letters = []  

def display_clue(word, guessed_letters):
    clue = ""
    for letter in word:
        if letter.lower() in guessed_letters or letter.upper() in guessed_letters:
            clue += letter + " "
        else:
            clue += "_ "
    return clue

while True:
    print(display_clue(word, guessed_letters))
    guess = input("Guess your letter: ").upper()  # Convert to uppercase for uniform comparison
    if guess in guessed_letters:
        print("You've already guessed that letter!")
        continue
    guessed_letters.append(guess)
    if all(letter.lower() in guessed_letters or letter.upper() in guessed_letters for letter in word):
        print(f"Congratulations! You guessed the word: {word}")
        break