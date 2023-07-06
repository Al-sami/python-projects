import random

def get_choices():
    player_choice = input("Enter rock/paper/scissor: ")
    options = ["rock", "scissor", "paper"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    if player == computer:
        return "It's a tie."
    elif player == "rock":
        if computer == "scissor":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."
    elif player == "paper":
        if computer == "scissor":
            return "Scissors cuts paper! You lose."
        else:
            return "Paper covers rock! You win!"
    elif player == "scissor":
        if computer == "rock":
            return "Rock smashes scissors! You lose."
        else:
            return "Scissor cuts paper! You win!"


choice = get_choices()
result = check_win(choice["player"], choice["computer"])
print(result)




