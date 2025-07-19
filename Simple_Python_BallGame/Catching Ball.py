import tkinter as tk
import random

# Constants
WIDTH = 400
HEIGHT = 500
BALL_SIZE = 20
PADDLE_WIDTH = 75
PADDLE_HEIGHT = 10
BALL_SPEED = 10
PADDLE_SPEED = 25

class CatchBallGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Catch The Falling Ball")

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.score = 0
        self.game_over_flag = False

        self.score_text = self.canvas.create_text(
            10, 10, anchor="nw", fill="white", font=("consolas", 16),
            text=f"Score: {self.score}"
        )

        self.paddle = self.canvas.create_rectangle(
            WIDTH//2 - PADDLE_WIDTH//2, HEIGHT - 40,
            WIDTH//2 + PADDLE_WIDTH//2, HEIGHT - 40 + PADDLE_HEIGHT,
            fill="white"
        )

        self.ball = self.canvas.create_oval(0, 0, BALL_SIZE, BALL_SIZE, fill="red")
        self.reset_ball()

        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)

        self.restart_button = None
        self.quit_button = None

        self.update_game()

    def reset_ball(self):
        x = random.randint(0, WIDTH - BALL_SIZE)
        self.canvas.coords(self.ball, x, 0, x + BALL_SIZE, BALL_SIZE)

    def move_left(self, event):
        x1, _, x2, _ = self.canvas.coords(self.paddle)
        if x1 > 0:
            self.canvas.move(self.paddle, -PADDLE_SPEED, 0)

    def move_right(self, event):
        _, _, x2, _ = self.canvas.coords(self.paddle)
        if x2 < WIDTH:
            self.canvas.move(self.paddle, PADDLE_SPEED, 0)

    def update_game(self):
        if self.game_over_flag:
            return

        self.canvas.move(self.ball, 0, BALL_SPEED)

        ball_coords = self.canvas.coords(self.ball)
        paddle_coords = self.canvas.coords(self.paddle)

        if self.check_collision(ball_coords, paddle_coords):
            self.score += 1
            self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
            self.reset_ball()
        elif ball_coords[3] >= HEIGHT:
            self.end_game()
            return

        self.root.after(30, self.update_game)

    def check_collision(self, ball, paddle):
        bx1, by1, bx2, by2 = ball
        px1, py1, px2, py2 = paddle
        return bx2 > px1 and bx1 < px2 and by2 >= py1 and by1 <= py2

    def end_game(self):
        self.game_over_flag = True
        self.canvas.create_text(
            WIDTH // 2, HEIGHT // 2 - 30, fill="red", font=("consolas", 24),
            text="GAME OVER"
        )

        # Add Restart Button
        self.restart_button = tk.Button(self.root, text="Restart", font=("consolas", 14),
                                        command=self.restart_game, fg="white", bg="green")
        self.restart_button.pack(pady=5)

        # Add Quit Button
        self.quit_button = tk.Button(self.root, text="Quit", font=("consolas", 14),
                                     command=self.root.destroy, fg="white", bg="red")
        self.quit_button.pack(pady=5)

    def restart_game(self):
        # Remove buttons
        if self.restart_button:
            self.restart_button.destroy()
        if self.quit_button:
            self.quit_button.destroy()

        # Reset game state
        self.score = 0
        self.game_over_flag = False
        self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")

        self.canvas.coords(
            self.paddle,
            WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 40,
            WIDTH // 2 + PADDLE_WIDTH // 2, HEIGHT - 40 + PADDLE_HEIGHT
        )

        self.reset_ball()
        self.canvas.delete("all")  # Clear all canvas items
        # Redraw score, paddle, ball
        self.score_text = self.canvas.create_text(
            10, 10, anchor="nw", fill="white", font=("consolas", 16),
            text=f"Score: {self.score}"
        )
        self.paddle = self.canvas.create_rectangle(
            WIDTH//2 - PADDLE_WIDTH//2, HEIGHT - 40,
            WIDTH//2 + PADDLE_WIDTH//2, HEIGHT - 40 + PADDLE_HEIGHT,
            fill="white"
        )
        self.ball = self.canvas.create_oval(0, 0, BALL_SIZE, BALL_SIZE, fill="red")
        self.reset_ball()
        self.update_game()

# Run the Game
if __name__ == "__main__":
    root = tk.Tk()
    game = CatchBallGame(root)
    root.mainloop()
