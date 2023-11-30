from tkinter import *
import time
import random

screen = Tk()
screen.title("Game")
screen.resizable(False, False)
canvas = Canvas(screen, width=500, height=500)
canvas.pack()
screen.update()


class Ball:
    def __init__(self, canvas, color, platform, score):
        self.canvas = canvas
        self.id = canvas.create_oval(0, 0, 20, 20, fill=color)
        self.canvas.move(self.id, 240, 240)
        cords = [-5, -4, -3, 3, 4, 5]
        self.x = random.choice(cords)
        self.y = -5
        self.platform = platform
        self.hit_bot = False
        self.score = score

    def hit_platform(self, pos):
        platform_pos = self.canvas.coords(self.platform.id)
        if pos[2] >= platform_pos[0] and pos[0] <= platform_pos[2]:
            if platform_pos[1] <= pos[3] <= platform_pos[3]:
                self.score.hit()
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 5
        elif pos[3] >= 500:
            self.hit_bot = True
            self.canvas.create_text(250,200, text="You lose", font=("Courier", 20, 'bold'), fill = "red")
        elif pos[2] >= 500:
            self.x = -3
        elif pos[0] <= 0:
            self.x = 3
        if self.hit_platform(pos):
            self.y = -10


class Platform:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 120, 18, fill=color)
        self.canvas.move(self.id, 220, 350)
        self.x = 0
        self.canvas.bind_all("<KeyPress-Left>", self.left)
        self.canvas.bind_all("<KeyPress-Right>", self.right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[2] >= 500:
            self.x = 0
        elif pos[0] <= 0:
            self.x = 0

    def left(self, event):
        self.x = -5

    def right(self, event):
        self.x = 5


class Score:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.score = 0
        self.id = self.canvas.create_text(25, 15,
                                          text=self.score,
                                          font=("Courier", 16),
                                          fill=color)
    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text=self.score)

score = Score(canvas, "blue")
platform = Platform(canvas, 'green')
ball = Ball(canvas, "red", platform, score)
while True:
    if ball.hit_bot == False:
        platform.draw()
        ball.draw()
    else:
        time.sleep(2)
        break
    screen.update_idletasks()
    screen.update()
    time.sleep(0.01)
