import random
options = ["rock", "paper", "scissors"]
while True:
    player1 = input("Enter Rock, Paper, or Scissor:").lower()
    player2 = random.choice(options).lower()
    
    if player1 == "quit" or player1=="q" or player1=="Quit".lower():
        break
    if player1 not in options:
        print("Invalid move. Please try again.")
        print('--------Enter "quit/q" for exit--------' )
        continue
    
    if player1=='rock' and player2=='paper':
        print("Computer won")
        print('--------Enter "quit/q" for exit--------' )

    elif player1 == 'paper' and player2=='scissor':
        print("Computer won")
        print('--------Enter "quit/q" for exit--------' )

    elif player1 == 'scissor' and player2 == 'rock':
        print("Computer won")
        print('--------Enter "quit/q" for exit--------' )

    elif player1 == player2:
        print("Tie!!!!")
        print('--------Enter "quit/q" for exit--------' )
    else:
        print("Congratulations!!! You won the game.")