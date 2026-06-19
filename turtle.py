import turtle

screen = turtle.Screen()


pen = turtle.Turtle()

for _ in range(4):
    pen.forward(100)  
    pen.left(90)    

screen.exitonclick()
