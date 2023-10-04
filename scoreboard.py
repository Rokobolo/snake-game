from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 18, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as data_file:
            self.high_score = int(data_file.read())
        self.score = 0
        self.goto(0, 265)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(arg=f"Score: {self.score} - High score: {self.high_score}", align=ALIGN, font=FONT)

    def scoring(self):
        self.score += 1
        self.score_update()

    def game_over(self):
        self.goto(0, 0)
        self.color("blue")
        self.write(arg="GAME OVER", align=ALIGN, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.score_update()

