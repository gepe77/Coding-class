import tkinter as tk
import random

 #setup game

winwd = 800
winhg =600

paddlewd =100
paddlehg =15

ballsize =20

brickrow = 6
brickcol = 9

brickhg = 15
birckwd = 100

#canvas
root = tk.Tk()
root.title("Ping Pong gaem")
canvas = tk.Canvas(root,width= winwd,height= winhg,bg= "black")
canvas.pack()
