import random

# word guess game
words = ["bright", "champs", "coding", "python", "student"]

# Di sini kita menggunakan fungsi choice()
word = random.choice(words)

# variabel untuk input text
name = input("Please enter the player's name: ")

# disini mendefinisikan variabel di sini dengan string.
guessedLetters = ""

# sejumlah peluang dapat digunakan di sini
chance = 10

print("Okay! ", name, "Let's start guessing.")

# Looping
while chance > 0:
    # disini akan mulai mengambil kata untuk diperiksa
    guess = input("Guess a letter of the word: ")

    # di guessedLetters kita akan menyimpan semua huruf yang telah kita sisipkan.
    guessedLetters += guess

    # disini memeriksa apakah semua pengguna salah atau benar.
    wrong = 0

    # disini semua huruf akan diperiksa satu per satu menggunakan loop
    for letter in word:
        # disini jika huruf yang dimasukkan pengguna ada di dalamnya, lalu cetak.
        if letter in guessedLetters:
            print(letter)

        else:
            print("_")
            wrong = 1

    # disini jika wrong adalah nol maka artinya semua kata cocok.
    if wrong == 0:
        print("Congratulations! ", name, "You guessed all the letters correct.")

        print("The word correct is: ", word)
        break

    # disini jika huruf yang kita tebak tidak ada dalam kata
    if guess not in word:
        # tidak ada peluang yang akan dikurangi 1
        chance -= 1  # tidak ada peluang yang akan dikurangi 1

        print("Wrong guess. This letter is not in word.")

        # disini akan memberitahukan berapa peluang pengguna yang terisa.
        print("You have", chance, "more guess chances. ")

        # Jika peluangnya nol, kami akan mencetak si pengguna kalah
        if chance == 0:
            print("Sorry! Your number of chances are over. You loose.")
