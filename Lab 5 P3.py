sides_number = int(input("Enter number of sides for polygon: "))
sides_length = int(input("Enter length of sides for polygon: "))
color = input("Enter a color for the outline of polygon: ")
color_fill = input("Enter a color to fill polygon: ")

import turtle
wn = turtle.Screen()
drawing = turtle.Turtle()
drawing.color(color)
drawing.fillcolor(color_fill)

drawing.begin_fill()

for i in range(sides_number):
    drawing.forward(sides_length)
    drawing.left(360 / sides_number)

drawing.end_fill()

#Victor Moreno
#2/16/24
#program asks the user for the number of sides, the length of the side, the color of the line, and the fill color of the polygon. The program draws the polygon and then fills it in
