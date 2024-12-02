import turtle
turtle.Screen().bgcolor("black")
turtle.Screen().setup(400,400)
cursor = turtle.Turtle()
cursor.color("red")
cursor.fillcolor("white")
for i in range(6):
    cursor.forward(70)
    cursor.left(60)
turtle.done()