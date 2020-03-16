# Write your code here
from random import choice
import  string

word_list = ["python", "java", "kotlin", "javascript"]
random_word = choice(word_list)
lives = 8
msg = list("-"*len(random_word))
attempts = set()
control = "play"

print("H A N G M A N")
while control != "exit":
    control = input('Type "play" to play the game, "exit" to quit: ')
    if control == "exit":
        break

    while lives and "-" in msg:
        print()
        print("".join(msg))
        letter = input("Input a letter: ")

        if len(letter) > 1:
            print("You should print a single letter")

        elif letter not in string.ascii_lowercase:
            print("It is not an ASCII lowercase letter")

        elif letter in attempts:
            print("You already typed this letter")

        else:
            attempts.add(letter)
            if letter in set(random_word):
                if letter not in set(msg):
                    for pos, char in enumerate(random_word):
                        if char == letter:
                            msg[pos] = letter
                else:
                    print("No improvements")
                    lives -= 1
            else:
                print("No such letter in the word")
                lives -= 1

    if control == "play":
        if "-" not in msg:
            print()
            print("".join(msg))
            print("You guessed the word!")
            print("You survived!")

        else:
            print("You are hanged!")
