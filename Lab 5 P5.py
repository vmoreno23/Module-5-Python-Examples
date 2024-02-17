import turtle
wn = turtle.Screen()
drawing = turtle.Turtle()

drawing.color("blue")
drawing.fillcolor("blue")

drawing.begin_fill()
for i in [1,2]:
    drawing.forward(210)
    drawing.right(90)
    drawing.forward(210)
    drawing.right(90)
drawing.end_fill()

drawing.fillcolor("red")
drawing.begin_fill()
drawing.color("red")
drawing.left(45)
drawing.forward(150)
drawing.right(90)
drawing.forward(148)
drawing.end_fill()

drawing.fillcolor("red")
drawing.begin_fill()
drawing.color("red")
drawing.forward(150)
drawing.right(90)
drawing.forward(150)
drawing.end_fill()

drawing.fillcolor("red")
drawing.begin_fill()
drawing.color("red")
drawing.forward(148)
drawing.right(90)
drawing.forward(150)
drawing.end_fill()

drawing.fillcolor("red")
drawing.begin_fill()
drawing.color("red")
drawing.forward(150)
drawing.right(90)
drawing.forward(150)
drawing.end_fill()


#Victor Moreno
#2/16/24
#Program draws a picutre of a blue square inside a red square. The red square is at a 45 degree angle 
