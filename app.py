# Write these rules for a python game, Rock betas scissors, scissors beats paper, paper beats rock
# Ask the user for their choice of rock, paper, scissors
# Have the computer choose its move
# Compare the choices and decide who wins
# Print the results
# Ask the user if they want to play again
# If yes, start the game again
# write a python program that will play rock paper scissors with the user
import random
import time
import sys

def play_again():
    while True:
        answer = input("Would you like to play again? y/n: ")
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Invalid input, please enter y or n")

def get_user_choice():
    while True:
        print("Please choose one of the following: ")
        print("Rock: r")
        print("Paper: p")
        print("Scissors: s")
        user_choice = input("Your choice: ")
        if user_choice == "r":
            return "rock"
        elif user_choice == "p":
            return "paper"
        elif user_choice == "s":
            return "scissors"
        else:
            print("Invalid input, please enter r, p, or s")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)

def print_result(user_choice, computer_choice):
    print_pause("You chose " + user_choice + ".")
    print_pause("The computer chose " + computer_choice + ".")
    if user_choice == computer_choice:
        print_pause("It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "paper":
            print_pause("Paper covers rock. You lose!")
        else:
            print_pause("Rock smashes scissors. You win!")
    elif user_choice == "paper":
        if computer_choice == "scissors":
            print_pause("Scissors cuts paper. You lose!")
        else:
            print_pause("Paper covers rock. You win!")
    elif user_choice == "scissors":
        if computer_choice == "rock":
            print_pause("Rock smashes scissors. You lose!")
        else:
            print_pause("Scissors cuts paper. You win!")

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print_result(user_choice, computer_choice)

def play():
    play_game()
    while play_again():
        play_game()
    print_pause("Thanks for playing!")

play()
