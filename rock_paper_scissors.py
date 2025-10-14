# rock paper scissor

import random

rock = '''
    _ _ _ _ _ _ 
---'      _ _ _)
        (_ _ _ _)
        (_ _ _ _)
        (_ _ _)
---._ _ (_ _)
'''

paper = '''
    _ _ _ _ _
---'    _ _ _ )_ _      
          _ _ _ _ _)
          _ _ _ _ _ _)  
         _ _ _ _ _)
---._ _ _ _ _ _)
'''

scissor = '''

    _ _ _ _ _
---'    _ _ _ )_ _      
          _ _ _ _ _)
          _ _ _ _ _ _)  
         (_ _ _)
---._ _ _(_ _ _)
'''
game_images=[rock, paper, scissor]


user_choise = int(input("what do you choose? Type 0 for rock, 1 for paper, 2 for scissor. \n"))
if user_choise >= 0 and user_choise <=2:
    print(game_images[user_choise])

computer_choise = random.randint(0,2)
print("computer chose, ")
print(game_images[computer_choise])

if user_choise >= 2 or user_choise < 0:
    print("You typed an invalid number. You Lose!")
elif user_choise == 0 and computer_choise == 2:
    print("You win!")
elif computer_choise == 0 and user_choise == 2:
    print("You Lose")
elif computer_choise > user_choise:
    print("You Lose!") 
elif user_choise > computer_choise:
    print("you win!")
elif computer_choise == user_choise:
    print("It's a Draw!")
