from turtle import Turtle
MOVE_DISTANCE = 20

# [East, North, West, South]
CARDINAL = [0, 90, 180, 270]


class Snake:
    def __init__(self):
        self.segment_l = []
        self.default_snake(3)
        self.head = self.segment_l[0]

    def default_snake(self, n):
        coorx = 0
        for x in range(n):
            self.new_part((coorx, 0))
            coorx -= 20

    def new_part(self, position):
        body = Turtle()
        body.penup()
        body.color("white")
        body.shape("square")
        body.goto(position)
        self.segment_l.append(body)
        return body

    def extend(self):
        self.new_part(self.segment_l[-1].pos())

    def move(self):
        for seg in range(len(self.segment_l) - 1, 0, -1):
            new_x = self.segment_l[seg - 1].xcor()
            new_y = self.segment_l[seg - 1].ycor()
            self.segment_l[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # [East, North, West, South]
    def move_up(self):
        if self.head.heading() != CARDINAL[3]:
            self.head.seth(CARDINAL[1])

    def move_down(self):
        if self.head.heading() != CARDINAL[1]:
            self.head.seth(CARDINAL[3])

    def move_left(self):
        if self.head.heading() != CARDINAL[0]:
            self.head.seth(CARDINAL[2])

    def move_right(self):
        if self.head.heading() != CARDINAL[2]:
            self.head.seth(CARDINAL[0])

    def reset_snake(self):
        for seg in self.segment_l:
            seg.goto(1000, 1000)
        self.segment_l.clear()
        self.default_snake(3)
        self.head = self.segment_l[0]