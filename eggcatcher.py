from tkinter import Canvas, Tk, messagebox, font
from random import randrange
from itertools import cycle


score = 0
lives = 3
canwd = 400
canhg = 400

root = Tk()
root.title("Egg Hunt")


c = Canvas(root, width=canwd, height=canhg, background="skyblue")
c.create_rectangle(-5, canhg - 5, canwd + 5, canhg + 5, fill="green", width=0)
c.create_oval(-80, -80, 120, 120, fill="yellow", width=10)
c.pack()


egg_colors = cycle(["lightblue", "lightgray", "lightgreen", "lightyellow"])
eggwd = 45
egghg = 55
eggscore = 10
speed = 200
egginterval = 800


bowlcolor = "red"
bowlwd = 60
bowlhg = 40
bowlstartx = canwd / 2 - bowlwd / 2
bowlstarty = canhg - bowlhg - 20

bowl = c.create_arc(bowlstartx, bowlstarty,bowlstartx + bowlwd, bowlstarty + bowlhg,start=200, extent=140, style="arc", outline=bowlcolor, width=4)


gamefont = font.Font(family="Arial", size=18)
score_text = c.create_text(10, 10, anchor="nw", font=gamefont, fill="darkblue", text="Score: 0")
lives_text = c.create_text(canwd - 10, 10, anchor="ne", font=gamefont, fill="darkblue", text="Lives: 3")


def move_bowl_left(event):
    x1, y1, x2, y2 = c.coords(bowl)
    if x1 > 0:
        c.move(bowl, -20, 0)

def move_bowl_right(event):
    x1, y1, x2, y2 = c.coords(bowl)
    if x2 < canwd:
        c.move(bowl, 20, 0)

root.bind('<Left>', move_bowl_left)
root.bind('<Right>', move_bowl_right)


def new_egg():
    x = randrange(10, canwd - eggwd - 10)
    return c.create_oval(x, -egghg, x + eggwd, 0, fill=next(egg_colors), width=0)

egg = new_egg()


def update_score(points):
    global score
    score += points
    c.itemconfigure(score_text, text="Score: " + str(score))


def lose_life():
    global lives
    lives -= 1
    c.itemconfigure(lives_text, text="Lives: " + str(lives))
    if lives <= 0:
        messagebox.showinfo("Game Over", "Final Score: " + str(score))
        root.destroy()


def egg_fall():
    global egg, speed, egginterval

    c.move(egg, 0, 20)
    eggx1, eggy1, eggx2, eggy2 = c.coords(egg)
    bowlx1, bowly1, bowlx2, bowly2 = c.coords(bowl)

    
    catch_zone_top = bowly1 - 15
    catch_zone_bottom = bowly2 + 5

    
    if (catch_zone_top <= eggy2 <= catch_zone_bottom) and (bowlx1 - 10 <= eggx1 <= bowlx2 + 10):
        update_score(eggscore)
        c.delete(egg)
        egg = new_egg()
        root.after(egginterval, egg_fall)

    
    elif eggy2 < canhg:
        root.after(speed, egg_fall)

    
    else:
        lose_life()
        c.delete(egg)
        if lives > 0:
            egg = new_egg()
            root.after(egginterval, egg_fall)

# Start the game
egg_fall()
root.mainloop()
