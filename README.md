# Alien Invasion (Star Wars Themed) game using pygame library

Alien Invasion is a game built using the pygame library. This README file provides instructions for building and running the game.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have installed Python 3.x.
- You have installed the pygame library or just install the requirements.txt depenedences.
- You have installed pyinstaller. You can install it using pip:
    ```sh
    pip install pyinstaller
    ```

## Building the Game

To build the game, use the following pyinstaller command which packages the `main.py` script along with the necessary data and image directories into a single executable file:
```sh
pyinstaller --onefile --add-data "data:data" --add-data "imgs:imgs" main.py
```

This will generate a `dist` directory containing the executable file.

## Running the Game

To run the game, navigate to the `dist` directory and execute the generated file:
- On Windows:
    ```sh
    dist\main.exe
    ```
- On macOS/Linux:
    ```sh
    ./dist/main
    ```

Enjoy playing Alien Invasion!

## To build the game: 
pyinstaller --onefile --add-data "data:data" --add-data "imgs:imgs" main.py

