# Pokemon-Game

This program is a simple Pokemon battle game where the user and the computer-controlled opponent select moves to attack each other's Pokemon until one of them faints.

## Prerequisites

- Python 3.x

## Getting Started

1. Clone the repository or download the Python script.

2. Run the Python script in a Python-compatible environment.

## How to Play

1. Upon running the script, you will be prompted to enter your chosen Pokemon from the given options.

2. The computer will randomly select its Pokemon.

3. The battle begins! You and the computer will take turns selecting moves to attack each other's Pokemon.The power of the same move may be different for different pokemon depending upon its type.

4. Moves are displayed with their corresponding numbers. Enter the number of the move you want to use.

5. The game continues until either your Pokemon or the computer's Pokemon faints.

6. The winner is announced, and the program exits.

## File Description

- `Moves.txt`: Contains the data for different moves, including their names, types, and power. The number of Pokemon can be increased by simply adding the data into the file Pokemon.txt (Maintain same format).

- `Pokemon.txt`: Contains the data for different Pokemon, including their names, types, and moves. If there are any new moves, add the data into Moves.txt(Maintain the same format)

## Program Structure

The program consists of the following main components:

- `Move` class: Defines a move with its name, type, power, and a power multiplier based on the Pokemon type.

- `Pokemon` class: Defines a Pokemon with its name, type, health, and four moves. The moves are initialized using the data from the `Moves.txt` file.

- `Display` function: Displays the user's Pokemon and its health, as well as the computer's Pokemon and its health.

- `UserPlay` function: Prompts the user to choose a move and deducts the corresponding power from the computer's Pokemon's health.

- `Result` function: Checks if either Pokemon has fainted and declares the winner.

- `CompPlay` function: Determines the move to be used by the computer's Pokemon based on move power and a random chance.

- Main Program: Asks the user to select their Pokemon, initializes the user's and computer's Pokemon, and continues the battle until a winner is determined.




