player1 = input("do you want rock, paper, or scissors?\n ")

player2 = input("do you want rock, paper, or scissors?\n ")

if player1 == player2:
    print("there is a tie")
elif player1 == 'paper' and player2 == 'rock':
    print("player 1 wins")
elif player1 == 'rock' and player2 == 'scissors':
    print("player 1 wins")
elif player1 == 'scissors' and player2 == 'paper':
    print("player 1 wins")
else:
    print("player 2 wins")