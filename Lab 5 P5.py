import turtle
wn = turtle.Screen()
drawing = turtle.Turtle()

drawing.color("blue") #sets outline to blue
drawing.fillcolor("blue") #sets fill color to blue 

drawing.begin_fill() #begins fill process 
for i in [1,2]: #draws square portion
    drawing.forward(210)
    drawing.right(90)
    drawing.forward(210)
    drawing.right(90)
drawing.end_fill() #ends fill process

#Draws top trangle portion
drawing.fillcolor("red")
drawing.begin_fill()
drawing.color("red")
drawing.left(45)
drawing.forward(150)
drawing.right(90)
drawing.forward(148)
drawing.end_fill()

#Draws right side triangle portion
drawing.fillcolor("red")
drawing.begin_fill()
drawing.color("red")
drawing.forward(150)
drawing.right(90)
drawing.forward(150)
drawing.end_fill()

#Draws bottom triangle portion
drawing.fillcolor("red")
drawing.begin_fill()
drawing.color("red")
drawing.forward(148)
drawing.right(90)
drawing.forward(150)
drawing.end_fill()

#draws left side triangle portion
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
