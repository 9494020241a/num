import turtle
import random

screen = turtle.Screen()
screen.title("Random 1–10 - 2s Pause")  # [docs] [1]
screen.setup(width=500, height=400)  # [docs] [1]

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.goto(0, 0)
t.color("black")  # [docs] [1]

def show_random():
    t.clear()  # remove previous number [guide] [13]
    n = random.randint(1, 10)  # 1–10 inclusive [ref] [6]
    t.write(str(n), align="center", font=("Arial", 72, "bold"))  # centered text [ref] [2]
    screen.ontimer(show_random, 2000)  # schedule next after 2000 ms [ref] [3]

show_random()  # kick off timer loop [ref] [3]
screen.mainloop()  # run event loop [docs] [1]
