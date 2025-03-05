#Fernando Guzman
#03/02/25

#Battle Module

import random, sys, time

wonBattle = 1
lostBattle = 2

def battle():
    while True:
        print("[A battle begins!]")
        result = random.randint(1, 100)
        if result %2 == 1:
            time.sleep(5)
            return wonBattle
        else:
            time.sleep(5)
            choice = input("You lost the battle. Game Over. (Try Again or Quit) ").strip().lower()
            if choice == 'try again':
                return battle()
            elif choice == 'quit' :
                return lostBattle
            else:
                print("Invalid choice! Please try again.")
                return battle()
            
