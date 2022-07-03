import turtle
import time
import random


def snake():
    delay = 0.1
    score = 0
    high_score = 0
    colors = random.choice(["red", "green", "black", "white", "yellow", "lime","dodgerblue","aqua"])
    window = turtle.Screen()
    window.title("Snake Game")
    window.bgcolor(colors)
    window.setup(width=600, height=600)
    window.tracer(89)

    # snake head
    head = turtle.Turtle()
    head.shape("square")
    head.color("red")
    head.penup()
    head.goto(0, 0)
    head.direction = "stop"

    # the foood

    food = turtle.Turtle()
    # colors=random.choice(["red","green","black"])
    shapes = random.choice(["square", 'triangle', "circle"])
    food.speed(0)
    food.shape(shapes)
    food.color(colors)
    food.penup()
    food.goto(0, 100)
    turtle.Screen().exitonclick()


if __name__ == '__main__':
    snake()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
