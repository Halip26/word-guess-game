import random


def choose_word():
    words = ["bright", "champs", "coding", "python", "student"]
    return random.choice(words)


def get_player_name():
    return input("Please enter the player's name: ")


def display_word(word, guessed_letters):
    print("-" * 35)
    for letter in word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()


def play_game():
    word = choose_word()
    player_name = get_player_name()
    guessed_letters = ""
    chances = 10

    print("-" * 35)
    print("Okay! {}, let's start guessing.".format(player_name))

    while chances > 0:
        guess = input("Guess a letter of the word: ").lower()
        guessed_letters += guess

        display_word(word, guessed_letters)

        if all(letter in guessed_letters for letter in word):
            print("-" * 35)
            print(
                "Congratulations! {} You guessed all the letters correctly.".format(
                    player_name
                )
            )
            print("The correct word is: {}".format(word))
            break

        if guess not in word:
            chances -= 1
            print("-" * 35)
            print("Wrong guess. This letter is not in the word.")
            print("You have {} more guess chances.".format(chances))

            if chances == 0:
                print("-" * 35)
                print("Sorry! Your number of chances are over. You lose.")
                print("The correct word was: {}".format(word))
                break


def main():
    play_game()


if __name__ == "__main__":
    main()
