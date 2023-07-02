import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

options = [rock, paper, scissors]

# User
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

print("You choose:")
user_selection = options[user_input]
print(user_selection)

# Computer
computer_input = random.randint(0, 2)
print("Computer chose: ")

computer_selection = options[computer_input]
print(computer_selection)

# Who wins?


if user_input >= 3 or user_input < 0:
    print("Invalid input.")
elif user_input == computer_input:
    print("It's a tie!")
elif (
    (user_input == 0 and computer_input == 2)
    or (user_input == 1 and computer_input == 0)
    or (user_input == 2 and computer_input == 1)
):
    print("You win!")
else:
    print("You lose :(")
