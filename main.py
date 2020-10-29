from computerInput import ComputerInput
from computerEyes import ComputerEyes
from build import Build


def main():
    print("program started")
    userInput = input(
        "1 - test eyes refresh, 2 - test all input, 3 - Play turn")
    bob = ComputerInput()
    rick = ComputerEyes()
    Ai = Build()

    if userInput == "1":
        print(rick.getSubshots()[1])
    elif userInput == "2":
        bob.buyCharacter(1)
    elif userInput == "3":
        Ai.playTurn()


if __name__ == '__main__':
    main()
