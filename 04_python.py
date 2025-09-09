import random
rock = ('''  
        _______
    ---'   ____)
            (_____)
            (_____)
    VK      (____)
    ---.__(___)
''')
Paper = ('''
        _______
    ---'   ____)____
                ______)
                _______)
    VK         _______)
    ---.__________)
            ''')
Seissors = (''' 
        _______
    ---'   ____)____
                ______)
            __________)
    VK      (____)
    ---.__(___)
''')
game_images = [rock, Paper, Seissors]
user_choice =int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
print(game_images[user_choice])
computer_choice = random.randint(0,2)
print("Computer chose: ")
print(game_images[computer_choice])
print(f"Computer chose: {computer_choice}")
if user_choice == 0 and computer_choice == 2:
    print("You wins!")
elif user_choice == 2 and computer_choice == 0:
    print("You Lose!")
elif computer_choice < user_choice:
    print("You win!")
elif computer_choice > user_choice:
    print("You Lose!!")
elif computer_choice == user_choice:
    print("It's a Drow! ")

else:
    print("You typed an invalid number. You lose!")