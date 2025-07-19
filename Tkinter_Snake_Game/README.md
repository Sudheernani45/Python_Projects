###📄 Line-by-Line Code Explanation

from tkinter import *
import random
import os
Imports:

tkinter: GUI creation

random: Random food placement

os: File check for high score

📏 Game Constants

GAME_WIDTH = 1000
GAME_HEIGHT = 600
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"
HIGH_SCORE_FILE = "highscore.txt"
Sets window size, snake cell size, colors, initial body size, and file to store the high score.

📊 Game State Variables

score = 0
direction = 'down'
difficulty_speed = {"Easy": 200, "Medium": 150, "Hard": 100}
SPEED = 150
restart_button = None
quit_button = None
snake = None
food = None
Initializes game state including default speed, direction, and placeholder variables for objects and buttons.

🧠 High Score Functions

def load_high_score():
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, 'r') as file:
            return int(file.read())
    return 0

def save_high_score(new_score):
    with open(HIGH_SCORE_FILE, 'w') as file:
        file.write(str(new_score))

high_score = load_high_score()
Loads high score from file, or returns 0 if file not found.

Saves high score to file.

🐍 Snake Class

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = [[0, 0] for _ in range(BODY_PARTS)]
        self.squares = [
            canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            for x, y in self.coordinates
        ]
Initializes snake with 3 body parts.

Uses canvas.create_rectangle() to draw each body part.

🍎 Food Class

class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")
Randomly places a red circle (food) on the canvas using create_oval.

🔁 Game Loop

def next_turn(snake, food):
    global score
    ...
    window.after(SPEED, next_turn, snake, food)
Moves the snake in the current direction.

If snake eats food:

Increases score

Spawns new food

Else:

Removes last segment

Checks for collisions.

Calls itself again using after() with a delay (based on difficulty).

🔄 Direction Control

def change_direction(new_direction):
    global direction
    ...
Prevents snake from reversing direction.

💥 Collision Detection

def check_collisions(snake):
    ...
Wall Collision: if snake hits window edges.

Self Collision: if snake overlaps its body.

☠️ Game Over Handler

def game_over():
    ...
Clears canvas and shows GAME OVER message.

Updates high score if necessary.

Displays Restart and Quit buttons.

🔁 Restart Function

def restart_game():
    ...
Resets all game variables.

Reinitializes snake and food.

Restarts the game loop.

🧩 Difficulty Selection

def choose_difficulty():
    ...
Opens a separate window to select difficulty.

Sets the SPEED and starts the game.

▶️ Start Game

def start_game():
    global snake, food
    snake = Snake()
    food = Food()
    next_turn(snake, food)
Called after difficulty is selected to launch the game loop.

🖼️ Window Setup

window = Tk()
window.title("Snake Game")
window.resizable(False, False)
Initializes main game window.


label = Label(window, text=f"Score: {score}  High Score: {high_score}", font=('consolas', 30))
label.pack()
Shows score and high score at the top.


canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()
Main game drawing area.

🖥️ Centering the Window

window.update()
...
window.geometry(f"{GAME_WIDTH}x{GAME_HEIGHT+50}+{x}+{y}")
Gets screen size and centers the window.

🎮 Keyboard Bindings

window.bind('<Left>', lambda event: change_direction('left'))
...
Binds arrow keys to change direction of the snake.

🚀 Launch Game with Difficulty Menu

choose_difficulty()
window.mainloop()
Starts with a difficulty selector.

Runs the Tkinter main event loop.
