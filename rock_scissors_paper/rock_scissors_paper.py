import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper="""    
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

user_choice = input("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors.").strip()



option_list = [rock, paper, scissors]
if user_choice in {"0","1","2"}:
    computer_choice= (random.randint(0,2))
    user = int(user_choice) 
    print("conputer_choice: " + f"{option_list[computer_choice]}"+ "\n")
    print("user choose: "+f"{option_list[user]}" + "\n")
    print("result is: " +"\n")

    if user == computer_choice:
        print("Draw!")
    elif (user == 0 and computer_choice == 1) or (user == 1 and computer_choice == 2) or (user == 2 and computer_choice == 0):
        print("You lose!")  
    else:
        print("You win!")


else: 
    print("please enter proper value.")