from turtle import *

class Circle:
    """Represents a Circle.
    
    attributes: radius, center.
    """
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __str__(self):
           return f'Circle with center: ({self.center}) and radius: ({self.radius}).'
          
    def draw(self):
        t = Turtle()
        t.penup()
        t.goto(self.center[0], self.center[1] - self.radius)  # move to bottom of circle
        t.pendown()
        t.circle(self.radius)
        t.hideturtle()
