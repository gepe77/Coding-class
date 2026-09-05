import turtle as t
import random


t.bgcolor("green")
ular = t.Turtle()
speed = 0
ular.shape("turtle")
ular.color("red")
ular.speed(speed)
ular.penup()
#pen up itu ga akan gambar garis pada saat bergerak seperti pensil yang diangkat lalu melukis
ular.hideturtle()

pelet = t.Turtle()
pelet.shape("circle")
pelet.color("yellow")
pelet.penup()
pelet.hideturtle()
pelet.speed(0)

text_turtle = t.Turtle()
text_turtle.write("press space to start", align="center", font=("Arial", 20, "normal"))
text_turtle.hideturtle()

score = 0
text_score = t.Turtle()
text_score.penup()
x = (t.window_width() // 2) - 50
y = (t.window_height() // 2) - 50
text_score.setposition(x, y)
text_score.write(f"Score: {score}", align="right", font=("Arial", 16, "normal"))

def place_pelet(pelet):
    x = random.randint(-t.window_width() // 2 + 20, t.window_width() // 2 - 20)
    y = random.randint(-t.window_height() // 2 + 20, t.window_height() // 2 - 20)
    pelet.setposition(x, y)
    pelet.hideturtle() 

def kanan():
    ular.right(90)
    ular.forward(20)

def naik():      
    ular.left(90)
    ular.forward(20)

def kiri():
    ular.left(90)
    ular.forward(20)

def turun():
    ular.right(90)
    ular.forward(20)



def start_game(ular, pelet, text_turtle, text_score):
    text_turtle.clear()
    ular.setposition(0, 0)
    ular.showturtle()
    place_pelet(pelet)
    t.listen()
    

    def move_ular(ular, pelet, text_score):
        t.onkey(kanan, "Right")
        t.onkey(kiri, "Left")
        t.onkey(naik, "Up")
        t.onkey(turun, "Down")
        t.listen()
    
    move_ular(ular, pelet, text_score)
    if ular.distance(pelet) < 20:
        global score
        score += 1
        text_score.clear()
        x = (t.window_width() // 2) - 50
        y = (t.window_height() // 2) - 50
        text_score.setposition(x, y)
        text_score.write(f"Score: {score}", align="right", font=("Arial", 16, "normal"))
        place_pelet(pelet)
    
    t.ontimer(lambda: move_ular(ular, pelet, text_score), 100)
    
    if ular.xcor() > t.window_width() // 2 or ular.xcor() < -t.window_width() // 2 or ular.ycor() > t.window_height() // 2 or ular.ycor() < -t.window_height() // 2:
        text_turtle.setposition(0, 0)
        text_turtle.write("Game Over", align="center", font=("Arial", 20, "normal"))
        ular.hideturtle()
        pelet.hideturtle()
    
t.onkey(lambda: start_game(ular, pelet, text_turtle, text_score), "space")
            







t.done()