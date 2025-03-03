#Fernando Guzman
#03/03/25

#Chapter Introduction that are displayed on each chapter before the choice module

import ChoiceModule

def intro_chapter(chapter_number):
    chapter_intros = {
        1: "A dry desert night, the harrowing winds blow through the Dagobah space station.",
        2: "A fire roars at the location of your home; you see two bandits running away from the scene of the crime onto a space craft.",
        3: "The flowing lava from the volcanoes on the planet Mustafar on the outer rim of the galaxy create a creepy aura.",
        4: "The howling screams of terror and laughter escape the menacing castle on the mountain top.",
        5: "Laughing comes out of the tallest tower in the castle, a glowing light shows the shadow of Count Dooku, the man that destroyed your home."
    }

    if chapter_number in chapter_intros:
        print(f"\n--- Chapter {chapter_number}: {chapter_intros[chapter_number]} ---")
    else:
        print("\n--- Unknown Chapter ---")

