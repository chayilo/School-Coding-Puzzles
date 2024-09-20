import turtle as t

wn = t.Screen()

def drawShape(sides):
    for i in range(sides):
        t.speed(0)
        t.forward(400/sides)
        t.left(360 / sides)
        
def jump(x, y, h):
    t.penup()
    t.goto(x, y)
    t.setheading(h)
    t.pendown()
    
def drawStar(size, numPoints):
    for i in range(numPoints):
        t.speed(0)
        t.forward(size)
        t.right(180)
        t.forward(size)
        t.right((numPoints-2)*180/numPoints)
    t.right((numPoints-2)*180/numPoints)/2
    for i in range(numPoints):
    
        t.right((numPoints-2)*180/numPoints)
        
    
drawStar(60, 1000)

wn.exitonclick()