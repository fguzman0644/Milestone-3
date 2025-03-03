#Fernando Guzman
#03/02/25

#Battle Module

import random

def battle(restart chapter):
    print("[A battle begins!]"
    result = random.randint(1, 100)
    if result %2 == 1:
        print("You won the battle!")
        choice_module()
    else:
        print("You lost the battle.")
        input(print("Game Over. (Try Again or Quit)")).strip().lower()
        if choice == 'try again':
            restart_chapter()
        elif choice == 'quit':
            print("Quitting game. Goodbye!")
        else:
            print("Invalid choice! Please try again.")
            
