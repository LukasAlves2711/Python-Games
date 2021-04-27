import random


def play():
    print_opening()
    secret_word = load_secret_word()

    correct_letters = initialize_correct_letters(secret_word)
    print(correct_letters)

    hang = False
    got_it_right = False
    errors = 0

    while not hang and not got_it_right:

        kick = initiate_kick()

        if kick in secret_word:
            get_correct_kick(kick, correct_letters, secret_word)
        else:
            errors += 1
            draw_gallows(errors)

        hang = errors == len(secret_word)
        got_it_right = "_" not in correct_letters
        print(correct_letters)

    if "_" not in correct_letters:
        prints_winner_message()
    else:
        prints_loser_message(secret_word)
    print("End game")


def print_opening():
    print("*****************************")
    print('****Welcome to Hang game!****')
    print("*****************************")


def load_secret_word():
    open("words.txt", "r")
    words = []  # List of words

    with open("words.txt") as file:
        for line in file:
            line = line.strip()
            words.append(line)

    file.close()

    number = random.randrange(0, len(words))  # To know the size of the list, position 0 to full length
    secret_word = words[number].upper()
    return secret_word


def initialize_correct_letters(words):
    return ["_" for _ in words]


def initiate_kick():
    kick = input("What is the letter? ")  # capitulate user input
    kick = kick.strip().upper()  # Regardless the entry is with spaces
    return kick


def get_correct_kick(kick, correct_letters, secret_word):
    index = 0  # display letter position
    for letter in secret_word:  # finds the position of the letter in the string
        if kick == letter:  # Can entry capital letter
            correct_letters[index] = letter
            print("I found the letter {} in position {}".format(letter, index))
        index += 1


def draw_gallows(errors):
    print("  _______     ")
    print(" |/      |    ")

    if errors == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if errors == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if errors == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if errors == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if errors == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if errors == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if errors == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def prints_winner_message():
    print("Congratulation, you win!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def prints_loser_message(secret_word):
    print("What a pity you were hanged!")
    print("The word was {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if __name__ == "__main__":
    play()
