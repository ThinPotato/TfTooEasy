from computerInput import ComputerInput
from computerEyes import ComputerEyes


def main():
    print("program started")
    userInput = input("1 - test eyes refresh, 2 - test all input")

    if userInput == "1":
        rick = ComputerEyes()
        print(rick.getSubshots()[1])
    elif userInput == "2":
        bob = ComputerInput()
        bob.buyCharacter(1)


if __name__ == '__main__':
    main()
