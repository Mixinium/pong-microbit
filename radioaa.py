import turtle
import time
import random
from microbit import *
radio.config(length=32, queue=3, channel=18, power=0, address=0x75626974, group=0, data_rate=radio.RATE_1MBIT)
radio.on()

# L'écran méga ouf de la mort qui tue
écran = turtle.Screen()
écran.title("Pong avec Microbit")
écran.bgcolor('white')
écran.setup(width=1000, height=600)

#Raquette droite
raquette_droite = turtle.Turtle()
raquette_droite.speed(0)
raquette_droite.shape("square")
raquette_droite.goto(0, -1000)
raquette_droite.goto(0, 1000)
raquette_droite.color("black")
raquette_droite.shapesize(stretch_wid=5, stretch_len=1)
raquette_droite.penup()
raquette_droite.goto(380, 0)
raquette_droite.dx = 15
raquette_droite.dy = -15

#Raquette gauche
raquette_gauche = turtle.Turtle()
raquette_gauche.speed(0)
raquette_gauche.shape("square")
raquette_gauche.color("black")
raquette_gauche.shapesize(stretch_wid=5, stretch_len=1)
raquette_gauche.penup()
raquette_gauche.goto(-380, 0)
raquette_gauche.dx = 10
raquette_gauche.dy = -10

#Balle
balle = turtle.Turtle()
balle.speed(0)
balle.shape("circle")
balle.color('purple')
balle.penup()
balle.dx = 10
balle.dy = -10

# Score
Joueur_1 = 0
Joueur_2 = 0

score = turtle.Turtle()
score.speed(0)
score.color("blue")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Joueur 1 : 0     Joueur 2 : 0",
         align="center", font=("Carlito", 24, "bold"))





def balnon():
    balle.goto(0, 0)

if random.randint(1, 25) == 0 :
        x = raquette_gauche.xcor()
        x += 60
        raquette_gauche.setx(x)
elif random.randint(1, 150) == 0 :
        x = raquette_gauche.xcor()
        x -= 20
        raquette_gauche.setx(x)

if random.randint(1, 150) == 0:
        xe = raquette_droite.xcor()
        xe += 20
        raquette_droite.setx(xe)
if random.randint(1, 25) == 0:
        xe = raquette_droite.xcor()
        xe -= 60
        raquette_droite.setx(xe)

while True:




#commandes
    if keyboard.is_pressed('z'):
        y = raquette_gauche.ycor()
        y += 15
        raquette_gauche.sety(y)
    if keyboard.is_pressed('s'):
        y = raquette_gauche.ycor()
        y -= 15
        raquette_gauche.sety(y)
    if keyboard.is_pressed('d'):
        x = raquette_gauche.xcor()
        x += 15
        raquette_gauche.setx(x)
    if keyboard.is_pressed('q'):
        x = raquette_gauche.xcor()
        x -= 15
        raquette_gauche.setx(x)

    if keyboard.is_pressed('up'):
        ye = raquette_droite.ycor()
        ye += 15
        raquette_droite.sety(ye)
    if keyboard.is_pressed('down'):
        ye = raquette_droite.ycor()
        ye -= 15
        raquette_droite.sety(ye)
    if keyboard.is_pressed('right'):
        xe = raquette_droite.xcor()
        xe += 15
        raquette_droite.setx(xe)
    if keyboard.is_pressed('left'):
        xe = raquette_droite.xcor()
        xe -= 15
        raquette_droite.setx(xe)

    # score
    if balle.xcor() >= 1000 :
        Joueur_1 += 1
        balnon()
    if balle.xcor() <= -1000 :
        Joueur_2 += 1
        balnon()

    #balle
    balle.setx(balle.xcor()+balle.dx)
    balle.sety(balle.ycor()+balle.dy)

    #bords
    if balle.ycor() > 280:
        balle.sety(280)
        balle.dy *= -1

    if balle.ycor() < -280:
        balle.sety(-280)
        balle.dy *= -1

    if raquette_droite.xcor() > 380:
        raquette_droite.setx(380)
        raquette_droite.dx *= -1

    if raquette_droite.xcor() < 0:
        raquette_droite.setx(-0)
        raquette_droite.dx *= -1

    if raquette_droite.ycor() > 280:
        raquette_droite.sety(280)
        raquette_droite.dy *= -1

    if raquette_droite.ycor() < -280:
        raquette_droite.sety(-280)
        raquette_droite.dy *= -1

    if raquette_gauche.xcor() > 0:
        raquette_gauche.setx(0)
        raquette_gauche.dx *= -1

    if raquette_gauche.xcor() < -380:
        raquette_gauche.setx(-380)
        raquette_gauche.dx *= -1

    if raquette_gauche.ycor() > 280:
        raquette_gauche.sety(280)
        raquette_gauche.dx *= -1

    if raquette_gauche.ycor() < -280:
        raquette_gauche.sety(-280)
        raquette_gauche.dx *= -1

    #scores
    if balle.xcor() > 500:
        balle.goto(0, 0)
        balle.dy *= -1
        Joueur_1 += 1
        score.clear()
        score.write("Joueur 1 : {}    Joueur 2 : {}".format(
                      Joueur_1, Joueur_2), align="center",
                      font=("Carlito", 24, "normal"))
        time.sleep(2)


    if balle.xcor() < -500:
        balle.goto(0, 0)
        balle.dy *= -1
        Joueur_2 += 1
        score.clear()
        score.write("Joueur 1 : {}    Joueur 2: {}".format(
                                 Joueur_1, Joueur_2), align="center",
                                 font=("Carlito", 24, "bold"))
        time.sleep(2)


    #Colisions
    if (balle.xcor() > 0 and balle.xcor() < 395) and (balle.ycor() < raquette_droite.ycor()+50 and balle.ycor()  > raquette_droite.ycor()-50 and balle.xcor() < raquette_droite.xcor()+20 and balle.xcor() > raquette_droite.xcor()-20):
        balle.setx(raquette_droite.xcor()-20)
        balle.dx *= -1
    if (balle.xcor() < -0 and balle.xcor() > -390) and (balle.ycor() < raquette_gauche.ycor()+50 and balle.ycor() > raquette_gauche.ycor()-50 and balle.xcor() < raquette_gauche.xcor()+20 and balle.xcor() > raquette_gauche.xcor()-20):
        balle.setx(raquette_gauche.xcor()+20)
        balle.dx *= -1


    if keyboard.is_pressed('esc'):
        exit()






    cimmu = radio.receive()
    if cimmu == "droite":
        if keyboard.is_pressed('right'):
            xe = raquette_droite.xcor()
            xe += 15
            raquette_droite.setx(xe)
    if cimmu == "gauche":
        if keyboard.is_pressed('left'):
            xe = raquette_droite.xcor()
            xe -= 15
            raquette_droite.setx(xe)
    if cimmu == "haut":
        if keyboard.is_pressed('up'):
            ye = raquette_droite.ycor()
            ye += 15
            raquette_droite.sety(ye)
    if cimmu == "bas":
        if keyboard.is_pressed('down'):
            ye = raquette_droite.ycor()
            ye -= 15
            raquette_droite.sety(ye)
