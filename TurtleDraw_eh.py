# TurtleDraw 
# By: Erick Hernandez
# Credits to Eric Pogue and W3C Python Tutorial

import turtle

print('TurtleDraw Starting...')

TEXTFILENAME = 'TurtleDraw.txt'
turtledrawText = open(TEXTFILENAME, 'r')
line = turtledrawText.readline()
while line:
    print(line, end='')
    line = turtledrawText.readline()
turtle.screensize(canvwidth=450, canvheight= 450)
#turtle.speed("fastest")

edTheTurtle = turtle.Turtle()
edTheTurtle.speed(speed=0)
edTheTurtle.forward(100)
edTheTurtle.right(90)
edTheTurtle.forward(100)
edTheTurtle.right(90)
edTheTurtle.forward(100)
edTheTurtle.right(90)
edTheTurtle.forward(100)

spiral = turtle.Turtle()
spiral.speed(speed=0)
for i in range(20):
    spiral.forward(i * 10)
    spiral.right(144)

turtle.done()