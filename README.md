# Text-Based Adventure Game

## Overview
This project is a Python-based text adventure game in which players progress through various chapters, each with its own set of challenges and characters. The game is structured into multiple chapters, with each chapter implemented as a separate Python file. The player interacts with the game by making choices that influence the story.

The game features a professor character and weapons that the player can use as they progress through the story.

## Game Files
- **start.py**: The main entry point to the game.
- **chapter1.py** to **chapter6.py**: These files represent different chapters of the game. Each file contains a specific storyline or challenges for the player.
- **professor.py**: Contains the `Professor` character's implementation with special attributes and methods.
- **Weapons**: A set of weapons, including a whip and a revolver, is available to the player and are introduced in certain chapters.

## Features
- **Modular Architecture**: Each chapter is stored in a separate Python file for ease of management and scalability.
- **Character Introduction**: As the player progresses, new characters like the `Professor` are introduced with unique abilities and dialogues.
- **Interactive Choices**: Players navigate the game by making decisions that affect the progression of the story.
- **Weapons**: Players can collect weapons like a whip and revolver, which are used in different parts of the game.

## Requirements
- **Python**: Version 3.x is required to run the game.
- **Platform**: Works on Windows, macOS, and Linux.
- **Libraries**: No external libraries are required; the game uses only the standard Python library.

## Installation and Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/YourRepositoryLinkHere
   cd YourRepositoryLinkHere
   ```
2. Ensure Python 3.x is installed by running:
   ```bash
   python3 --version
   ```

3. Run the game by executing:
   ```bash
   python3 start.py
   ```

## Game Structure
The game is split into different chapters, each representing a different section of the story. Below is a brief description of each file and its role in the game:

- **start.py**: Initializes the game and presents the main menu or first chapter of the story.
- **chapter1.py**: The first chapter of the game, where the player is introduced to the world and the initial challenges.
- **chapter2.py**: Continuation of the player's journey, introducing new challenges and environments.
- **chapter3.py**: The story deepens, and more choices are introduced.
- **chapter4.py**: New enemies and weapons are introduced, advancing the storyline.
- **chapter5.py**: Further progression into the game's plot, with more complex interactions.
- **chapter6.py**: The final chapter of the game, where the player faces the ultimate challenge.
- **professor.py**: Implements the `Professor` character, who interacts with the player during the game.

## How to Play
- After running the game using `python3 start.py`, you will be prompted with decisions that guide the narrative.
- Weapons and characters will be introduced as the game progresses, allowing players to collect and use items.
- Follow the prompts on the screen to navigate through the game's story.

## Development Notes
### Naming Conventions
- **Classes**: `CamelCase` (e.g., `Professor`, `Character`)
- **Functions and Variables**: `snake_case` (e.g., `start_game()`, `player_name`)
- **Constants**: All caps (e.g., `MAX_LIVES`)

### Game Logic
- Each chapter file contains its own story progression logic. When the player finishes a chapter, the game moves on to the next.
- The player can interact with characters, including the `Professor`, who will offer assistance or challenges.

## Contribution
Feel free to fork the repository and submit a pull request with any improvements or bug fixes. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.
