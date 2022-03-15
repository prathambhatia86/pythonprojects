import turtle
import pygame
pygame.init()
pygame.mixer.music.load("days-to-remember-18539.mp3")
pygame.mixer.music.play(-1)
bg=turtle.Screen()
bg.bgcolor("black")
bg.title("turtle")
tur=turtle.Turtle()
turs=turtle.Turtle()
heartss=turtle.Turtle()
turs.up()
turs.sety(150)
turs.setx(-350)
turs.down()
tur.ht()
tur.up()
turs.ht()
tur.sety(-250)
tur.color("white")
heartss.ht()
heartss.setx(-150)

tur.down()
tur.seth(30)
tur.speed(5)
turs.color("white")
turs.speed(1)
heartss.sety(-150)
heartss.color("white")
x=0

while True:


    def curve():
        for i in range(50):
            tur.right(1)
            tur.forward(1)

    def curvess():
        for i in range(200):
            heartss.right(1)
            heartss.forward(1)

    turs.write("happy marriage anniversary to didi and jiju",font=("monotype corsiva",30,"bold"))


    if(x==0):
        heartss.left(140)
        heartss.forward(200)
        curvess()
        heartss.left(140)
        curvess()
        heartss.forward(200)
        x+=1

    tur.goto(100, 0)
    curve()








tur.done()