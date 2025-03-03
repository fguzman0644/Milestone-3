#Fernando Guzman
#03/02/25

#Sequential choice Module
#Had help from family members familiar Python and some Google searches. I'll specify where

class AdventureGame:
    def __init__(self):
        self.chapter = 1 #Starts at chapter 1
        self.options = {
            1: ["Speak to bartender", "Talk to tavern patrons"],
            2: ["Chase bandits", "Run to burning house"],
            3: ["Take long way around", "Jumpt through shortcut"],
            4: ["Walk into castle", "Go into drawbridge tower"],
            5: ["Enter Boss room", "Pull suspicious torch lever"]
        }

    def choice_module(self):

        current_options = self.options.get(self.chapter, ["Option 1", "Option 2"])
##This gets the options for the current chapter
        current_options.append("Leave location")
        current_options.append("Return to last chapter")

        for index, option in enumerate(current-options, start=1):
##Had to Google how to tackle this section, decided to use enumerate to loop through options starting at 1 so user sees numbered list
            print(f"{index}.{option}")
            
        user_choice = input("Enter the number of your choise: ").strip()

        if user_choice.isdigit() and 1 <= int(user_choice) <= len(current_options):
##States if choice is between 1 and number of options on the list
            selected_choice = current_options[int(user_choice) - 1]
            self.process_choice(selected_choice)
        else:
            print("Invalid choice! Please try again")
            self.choice_module() #Asks again for valid choice

    def process_choice(self, choice):
        if choice == "Leave location":
            self.chapter += 1 if self.chapter < 5 else 0 #Moves user to next chapter if chapter less than 5. Asked family about this
        elif choice == "Return to last chapter":
            self.chapter -= 1 if self.chapter > 1 else 0 #Moves user to last chapter if chpater greater than 1. Asked family about this
        else:
            pass #Handle other choices here

        self.choice_module() #continue to the next choice
