# import colorgram

# colors = colorgram.extract('100-Days-of-Python\Day_018\Day_018_review\hirst-painting.PNG', 6)
# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
from turtle import Turtle , Screen ,colormode
import random



color_list = [(249, 248, 246), (251, 247, 249), (240, 249, 244), (239, 244, 249), (239, 221, 113), (19, 111, 193)]


tim = Turtle()
colormode(255)
tim.shape("circle")
tim.speed("fast")
tim.pensize(20)
n = -200
m = -200
h = 0
while True:    
    a = tim.fillcolor(random.choice(color_list))
    tim.penup()
    tim.goto(n,m)
    tim.dot(20,random.choice(color_list))
    tim.pendown()
    n +=50
    h +=1
    if h == 10 :
        h = 0
        m += 50
        n = -200
    if m == 300:
        break
    









screen = Screen()
screen.exitonclick()