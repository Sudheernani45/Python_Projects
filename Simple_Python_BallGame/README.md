###🎮 Line-by-Line Code Explanation

import tkinter as tk
import random
tkinter: For GUI.

random: To randomly position the ball.

⚙️ Constants

WIDTH = 400
HEIGHT = 500
BALL_SIZE = 20
PADDLE_WIDTH = 75
PADDLE_HEIGHT = 10
BALL_SPEED = 10
PADDLE_SPEED = 25
Define canvas size, ball and paddle dimensions, and movement speed.

🎮 Game Class

class CatchBallGame:
    def __init__(self, root):
Main class to control game logic and UI.

🎨 Canvas and UI Setup

        self.root = root
        self.root.title("Catch The Falling Ball")

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()
Sets the window title and creates a canvas for the game with a black background.

🧮 Initial Score & Game State

        self.score = 0
        self.game_over_flag = False
Keeps track of current score and game over status.


        self.score_text = self.canvas.create_text(
            10, 10, anchor="nw", fill="white", font=("consolas", 16),
            text=f"Score: {self.score}"
        )
Displays the score at the top-left corner.

⛳ Paddle Setup

        self.paddle = self.canvas.create_rectangle(
            WIDTH//2 - PADDLE_WIDTH//2, HEIGHT - 40,
            WIDTH//2 + PADDLE_WIDTH//2, HEIGHT - 40 + PADDLE_HEIGHT,
            fill="white"
        )
Creates a white paddle near the bottom of the screen.

🔴 Ball Setup


        self.ball = self.canvas.create_oval(0, 0, BALL_SIZE, BALL_SIZE, fill="red")
        self.reset_ball()
A red ball is drawn and placed randomly using reset_ball().

⌨️ Keyboard Bindings

        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
Left/Right arrow keys control paddle movement.

🔄 Buttons Placeholders

        self.restart_button = None
        self.quit_button = None
Will be used after game over.

🔁 Start Game Loop

        self.update_game()
Starts the ball falling and game updates.

🎯 Reset Ball Function

    def reset_ball(self):
        x = random.randint(0, WIDTH - BALL_SIZE)
        self.canvas.coords(self.ball, x, 0, x + BALL_SIZE, BALL_SIZE)
Moves the ball to the top at a random horizontal position.

👈👉 Paddle Movement

    def move_left(self, event):
        x1, _, x2, _ = self.canvas.coords(self.paddle)
        if x1 > 0:
            self.canvas.move(self.paddle, -PADDLE_SPEED, 0)

    def move_right(self, event):
        _, _, x2, _ = self.canvas.coords(self.paddle)
        if x2 < WIDTH:
            self.canvas.move(self.paddle, PADDLE_SPEED, 0)
Prevents paddle from moving off-screen.

🕹️ Game Update Loop

    def update_game(self):
        if self.game_over_flag:
            return

        self.canvas.move(self.ball, 0, BALL_SPEED)
Moves the ball down by BALL_SPEED.


        ball_coords = self.canvas.coords(self.ball)
        paddle_coords = self.canvas.coords(self.paddle)
Gets current positions of ball and paddle.


        if self.check_collision(ball_coords, paddle_coords):
            self.score += 1
            self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
            self.reset_ball()
        elif ball_coords[3] >= HEIGHT:
            self.end_game()
            return
Checks if the ball hits the paddle → +1 score.

If it hits the bottom, the game ends.


        self.root.after(30, self.update_game)
Continuously calls update_game() every 30 ms.

🧱 Collision Detection

    def check_collision(self, ball, paddle):
        bx1, by1, bx2, by2 = ball
        px1, py1, px2, py2 = paddle
        return bx2 > px1 and bx1 < px2 and by2 >= py1 and by1 <= py2
Simple AABB collision check.

❌ Game Over UI

    def end_game(self):
        self.game_over_flag = True
        self.canvas.create_text(WIDTH // 2, HEIGHT // 2 - 30, fill="red", font=("consolas", 24), text="GAME OVER")
Shows "GAME OVER" text.


        self.restart_button = tk.Button(...)
        self.quit_button = tk.Button(...)
Adds Restart (green) and Quit (red) buttons.

🔁 Restart Function

    def restart_game(self):
        if self.restart_button:
            self.restart_button.destroy()
        if self.quit_button:
            self.quit_button.destroy()
Destroys old buttons.


        self.score = 0
        self.game_over_flag = False
        self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
Resets game state.


        self.canvas.coords(...)  # Resets paddle position
        self.reset_ball()
        self.canvas.delete("all")  # Clears everything

        self.score_text = self.canvas.create_text(...)  # Redraw score
        self.paddle = self.canvas.create_rectangle(...)  # Redraw paddle
        self.ball = self.canvas.create_oval(...)  # Redraw ball
        self.reset_ball()
        self.update_game()
Completely rebuilds the game from scratch.

▶️ Game Launch

if __name__ == "__main__":
    root = tk.Tk()
    game = CatchBallGame(root)
    root.mainloop()
Creates and starts the game window.
