import random













def get_choice():


    player_choice = input("Enter your choice('rock', 'paper', or 'scissors'): ")
    computer_choice = "Paper"
    choices= {"player": player_choice, "computer": computer_choice}

    return choices

select= get_choice()
print(select)




choices= get_choice()
print(choices)


dict= {"name": "beau", "color": "blue", "age": 25}


def get_choice():


    player_choice = input("Enter your choice('rock', 'paper', or 'scissors'): ")
    options= ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    choices= {"player": player_choice, "computer": computer_choice}

    return choices

choices= get_choice()
print(choices)


foods= ["pizza", "burger", "sushi", "pasta", "salad"]
dinner= random.choice(foods)
print(dinner)

def check_win(player, computer):
    print(f"You chose: {player}, Computer chose: {computer}")

    if player == computer:
        return "It's a tie!"

    elif player == "rock":
        if computer == "scissors":
            return "rock smashes scissors! You win!"
        else:
            return "paper covers rock! Computer wins!"

    elif player == "paper":
        if computer == "rock":
            return "paper covers rock! You win!"
        else:
            return "scissors cuts paper! Computer wins!"

    elif player == "scissors":
        if computer == "paper":
            return "scissors cuts paper! You win!"
        else:
            return "rock smashes scissors! Computer wins!"

    else:
        return "Invalid choice!"

check_win("rock", "scissors")
result= check_win("rock", "scissors")
print(result)

choices= get_choice()
result= check_win(choices['player'], choices['computer'])
print(result)

 





    