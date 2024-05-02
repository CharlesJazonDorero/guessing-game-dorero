# Number Guessing Game

This is a simple client-server Number Guessing Game implemented in Python using socket programming. The game allows a player to guess a randomly generated number within a specified range and difficulty level. The server keeps track of the number of attempts made by each player and maintains a leaderboard of the best scores.

## Features

- Allows multiple clients to connect simultaneously and play the game.
- Supports three difficulty levels: Easy, Medium, and Hard, with different ranges for the randomly generated number.
- Displays the number of attempts made by the player to guess the correct number.
- Updates and saves the leaderboard with the best scores for each player.

## Requirements

- Python 3.x
- JSON module (comes pre-installed with Python)

## How to Run

Step 1. Clone the repository or download the source code.
Step 2. Open two terminal windows or command prompts.
Step 3. In one terminal window, navigate to the server directory.
Step 4. Run the server script by executing the following command:
    ```
    python server.py
    ```
Step 5. In the other terminal window, navigate to the client directory.
Step 6. Run the client script by executing the following command:
    ```
    python client.py
    ```
Step 7. Follow the on-screen instructions to play the game. Enter your name, choose the difficulty level, and start guessing numbers.

## Files Included

- `server.py`: Contains the server-side code for handling client connections, generating random numbers, and updating the leaderboard.
- `client.py`: Contains the client-side code for connecting to the server, sending player information, and making guesses.
- `leaderboard.json`: JSON file used to store and update the leaderboard data.

## Contributors

- Charles Jazon Y. Dorero

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

