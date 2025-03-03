#Fernando Guzman
#03/03/25

#Main module that links all other ones together

import time, BattleModule, ChoiceModule, StartModule, IntroModule

def main():
    player_name = StartModule.start_game()
    game = ChoiceModule
    while game.chapter <= 5:
        IntroModule.introduce_chapter(game.chapter)
        game.ChoiceModule()
        if game.chapter == 6:
            BattleModule.battle(game, player_name)
            break

StartModule.start_game()

