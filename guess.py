import random


def play():
    print("*****************************")
    print("Welcome to the guessing game!")
    print("*****************************")

    secret_number = random.randrange(1, 101)
    total_attempts: int = 0
    points = 1000

    print("what is the level of difficulty? ")
    print("(1) Easy (2) Normal (3) Hard ")

    level = int(input("Define the level: "))

    if level == 1:
        total_attempts = 20
    elif level == 2:
        total_attempts = 10
    else:
        total_attempts = 5

    for round in range(1, total_attempts + 1):
        print("Attempts {} of {}".format(round, total_attempts))
        kick_str = input('Type a number between 1 and 100: ')
        print("You typed: ", kick_str)
        kick = int(kick_str)

        if kick < 1 or kick > 100:
            print('You should type a number between 1 and 100!')
            continue

        win = kick == secret_number
        bigger = kick > secret_number
        less = kick < secret_number

        if win:
            print("It looks like we have a lucky guy!\n You won !!!")
            print("Your score was {} points".format(points))
            break
        else:
            if bigger:
                print("Try again! Your kick was bigger")
            elif less:
                print("Try again! Your kick was less")
            lost_points = abs(secret_number - kick)
            points = points - lost_points

        round = round + 1

    print("End game")


if __name__ == "__main__":
    play()
