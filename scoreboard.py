from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.current_score = 0
        self.penup()
        self.goto(-40, 250)
        self.pendown()
        self.write(f"Score: {self.current_score}", font=("Arial", 16, "normal"))


    def update(self, current_score):
        self.clear()
        self.speed('fastest')
        self.write(f"Score: {current_score}", font=("Arial", 16, "normal"))
        