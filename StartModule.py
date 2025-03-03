#Fernando Guzman
#03/02/25

#Start Module

import time, BattleModule, IntroModule, ChoiceModule

# Declare global variable
player_name = ""

def start_game():
    global player_name
    player_name = input("Welcome bounty hunter! What is your name? ")
    print(f"Hello, {player_name}! Your adventure begins now.")
    time.sleep(1)

start_game()
IntroModule.intro_chapter(1)
ChoiceModule.AdventureGame.choice_module(1)
