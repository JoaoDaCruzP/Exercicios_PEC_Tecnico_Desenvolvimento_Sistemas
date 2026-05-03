from turtle import *

shape('turtle')
speed(5)

#desenhando um pentagono

for i in range(5):
    forward(100)
    right(360 / 5)

clear()

#desenhando um hexagono

for  i in range(6):
    forward(100)
    right(360 / 6)

clear()

#desenhando um circulo
speed(11)
for i in range(360):
    forward(2)
    right(1)
done()