# game.py

import random
from constants import CHOICES, EMOJIS, ROCK, PAPER, SCISSORS


def get_user_choice() -> str:
    """Prompt until the user enters a valid choice."""
    while True:
        user_choice = input("Rock, paper, or scissors? (r/p/s): ").strip().lower()

        if user_choice in CHOICES:
            return user_choice

        print("Invalid choice.")


def get_computer_choice() -> str:
    """Randomly pick one of the valid choices."""
    return random.choice(CHOICES)


def display_choices(user_choice: str, computer_choice: str) -> None:
    """Print user and computer choices using emojis."""
    print(f"You chose {EMOJIS[user_choice]}")
    print(f"Computer chose {EMOJIS[computer_choice]}")


def determine_winner(user_choice: str, computer_choice: str) -> None:
    """Determine and print the result."""
    if user_choice == computer_choice:
        print("Tie!")
        return

    user_wins = (
        (user_choice == ROCK and computer_choice == SCISSORS)
        or (user_choice == SCISSORS and computer_choice == PAPER)
        or (user_choice == PAPER and computer_choice == ROCK)
    )

    if user_wins:
        print("You win!")
    else:
        print("You lose!")


def play_game() -> None:
    """Main game loop."""
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print()  # line break "paragraph" separation
        display_choices(user_choice, computer_choice)

        print()
        determine_winner(user_choice, computer_choice)

        print()
        should_continue = input("Continue? (y/n): ").strip().lower()
        if should_continue == "n":
            break

        print()  # spacing before next round
