import random
choices = ["rock", "paper", "scissors"]
while True:
    player1 = input("Enter Rock, Paper, or Scissor:").lower()
    player2 = random.choice(choices).lower()
    
    if player1 == "quit":
        break
    if player1 not in choices:
        print("Invalid move. Please try again.")
        continue
    
    if player1=='rock' and player2=='paper':
        print("Computer won")
    elif player1 == 'paper' and player2=='scissor':
        print("Computer won")
    elif player1 == 'scissor' and player2 == 'rock':
        print("Computer won")
    elif player1 == player2:
        print("Tie!!!!")
    else:
        print("Congratulations!!! You won the game.")