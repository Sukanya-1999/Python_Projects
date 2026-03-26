"""
WORKFLOW OF PROJECT
1 - Input from user(Rock, Paper, Scissor)
2- Computer choice(comouter will choose randomly not conditionally)
3- Result print

cases:
A- Rock
Rock - Rock = tie
Rock - paper = paper win 
Rock - scissor = Rock wins

B- Paper
Paper- paper = tie
Paper - Rock = Paper win
paper = scissor = scissor win

C- Scissor
Scissor - scissor = tie
scissor - Rock = Rock win 
Scissor - paper = scissor win


"""

import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move = Rock, Paper, Scissor=")
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both Chooses same: = Match Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock = Computer win")
    else:
        print("Rock smashes Scissor = You win")

elif user_choice == "Paper":
    if comp_choice == "Rock":
        print("Paper covers Rock = You win") 

    else:
        print("Scissor cuts paper = Computer win")   

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts paper = You win")
    else:
        print("Rock smashes scissor = computer win")

                            
      

