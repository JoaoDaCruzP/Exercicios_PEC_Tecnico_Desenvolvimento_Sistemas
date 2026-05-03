from turtle import *

lados = 16
angulo = 360 / lados

shape('turtle')
speed(8)
pensize(5)
color('blue')


for i in range(lados):
    forward(50)
    right(angulo)

done()
