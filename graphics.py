import turtle

turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)

turtle.right(30)
for square in [0,1,2,3]:
    turtle.forward(100)
    turtle.right(90)
turtle.done()               # to avoid closing window

