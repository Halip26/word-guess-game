import random

words_list = ["cat", "dog", "bag", "fat", "rat", "out", "run", "fun", "bed", "food"]

# use choice function to randomized the word
randomized_words = random.choice(words_list)

# input name from users
name = str(input("\nPlease enter your name: "))

# define variable guessed letters with empty str
guessed_letters = ""

# users only have 5 chances
max_attempts = 5

print(f"Okay {name}, You have {max_attempts} attempts, let's start guessing!")

print("-" * 35)

# print the list of words on console
print("\nList of words you have to guess: ")

for i in words_list:
    print("- ", i)

# use while loopuing with condition
while max_attempts > 0:
    # just created lines
    print("-" * 35)
    user_guess = str(input("Guess a letter of the word: "))

    # guessed_letters will save all letters yg entered
    guessed_letters += user_guess

    # declare wrong variable
    wrong = 0

    # check every word & character one by one using loops
    for letter in randomized_words:
        # here we will print the letter
        if letter in guessed_letters:
            print(letter)

        else:
            print("-")
            # wrong increased
            wrong = 1

    if wrong == 0:
        print(f"\nCongratulations! {name} You guessed all the letters correct")

        print(f"The word correct is {randomized_words}")
        break

    if user_guess not in randomized_words:
        max_attempts -= 1

        print("Wrong guess! This letter is not in words")

        print(f"You have {max_attempts} attempts left")

        if max_attempts == 0:
            print("Sorry! Your number of attempts are zero, It means you lost")
