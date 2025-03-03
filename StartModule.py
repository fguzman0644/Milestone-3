#Fernando Guzman
#03/02/25

#Start Module

import time
import BattleModule
import ChoiceModule

def start_game():
    global player_name
    player_name = input("Welcome bounty hunter! What is your name? ")
    print(f"Hello, {player_name}! Your adventure begins now.")
    time.sleep(1)
   IntroModule()
    
if __name__ == "__main__":
    start_game()
