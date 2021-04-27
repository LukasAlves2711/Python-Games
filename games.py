import To_hang
import guess


def choose_game():
    print("*****************************")
    print('******Choose your game!******')
    print("*****************************")

    print("(1) To hang game (2) Guessing game")

    game = int(input("What game would you like to play?"))

    if game == 1:
        print("Playing To hang game ")
        To_hang.play()
    elif game == 2:
        print("Playing Guessing game")
        guess.play()
    print("End game")


if __name__ == "__main__":
    choose_game()
