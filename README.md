# STAR HUNTER

## """Technical Document for Star Hunter game
The code is intended to be hosted on a standard file system or a version control system like GitHub. This game does not utilize any external services. It is a stand-alone Python application and will use Python 3.13, the latest version of Python. Some system requirements and supported applications are:
•	Python 3.x interpreter installed.
•	Standard terminal or command-line interface.
•	No specific operating system requirements (cross-platform).
The coding/naming conventions are for module, variable, function, and class names, costants, docstrings, and comments. Module names are formatted in lowercase and uppercase with no spaces (e.g., “BattleModule”, “v2BountyHunter”). Variable names are formatted with lowercase and underscores for separation (e.g., “player_name”, “chapter_number”). Function names with lowercase then uppercase with underscores for separation (e.g., “beginGame”, “run_game”); class names are formatted similarly (e.g., “chapterContent”). Constants with lowercase then uppercase (e.g., “wonBattle”, “lostBattle”). Docstrings are used for clarity within functions and classes, while comments are used to explain non-obvious code logic.
To run the program, ensure Python 3.13 is installed and save the provided code (e.g., “title.py”, “BattleModule.py”, “v2BountyHunter.py”) as `.py` files. Open a terminal or command prompt and navigate to the directory containing the saved files. Execute the main script (“v2BountyHunter.py”) using the command: “python v2BountyHunter.py”. No build or deployment steps are required as it's a simple Python script.
The game is structured into three main modules:
•	“title.py”: Handles the game's title display and introductory information.
•	“BattleModule.py”: Manages the battle logic, determining the outcome of battles.
•	“v2BountyHunter.py”: Contains the main game logic, including chapters, player interaction, and game flow.
The “v2BountyHunter.py” module imports and utilizes the functionalities of “title.py” and “BattleModule.py”. The game progresses through a series of chapters, each with an introduction and a battle. The “chapterContent” class encapsulates the introduction and battle descriptions for each chapter. The game uses user input to control the flow, including starting the game, engaging in battles, and continuing to the next chapter. The “BattleModule” module utilizes random number generation to determine battle outcomes. To start the program:
•	Run the “v2BountyHunter.py” script using the Python interpreter: “python v2BountyHunter.py”.
•	The game will display the title and introductory information.
•	The player will be prompted to enter their name.
•	The player will be asked if they are ready to start the adventure.
•	The player will then be prompted to fight battles and continue through the chapters."""
