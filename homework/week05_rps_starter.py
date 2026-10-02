# Rock Paper Scissors — Starter
# Software Programming (IGS1931)
#
# Name:          <your name>
# Student ID:    <your student ID>
# Levels completed (e.g. 1, 2, 3, 4):  <fill in>
#
# Keep improving THIS file level by level. Leave a comment like
# "# LEVEL 2" above the code you changed so the grader can find it.
# Run it with:  python3 week05_rps_starter.py

import random


def play():
    player = input("rock, paper or scissors? ")

    number = random.randint(1, 3)
    if number == 1:
        computer = "rock"
    elif number == 2:
        computer = "paper"
    else:
        computer = "scissors"
    print("Computer chose:", computer)

    if player == computer:
        print("Draw!")
    elif (player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):
        print("You win!")
    else:
        print("You lose!")


if __name__ == "__main__":
    play()
