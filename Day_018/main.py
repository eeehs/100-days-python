from turtle import Turtle , Screen



tt = Turtle()

tt.shape("turtle")

tt.color("blue")

# 1. 점선그리기 
# for _ in range(10):
#     tt.forward(10)
#     tt.penup()
#     tt.forward(10)
#     tt.pendown()

# 2. 다양한 도형 그리기 
def draw_triangele(x):
    for _ in range(3):
        tt.forward(x)
        tt.right(120)

def draw_square(x):
    for _ in range(4):
        tt.forward(x)
        tt.right(90)

def draw_pentagon(x):
    for _ in range(5):
        tt.forward(x)
        tt.right(72)

def draw_hexagon(x):
    for _ in range(6):
        tt.forward(x)
        tt.right(60)

def draw_Heptagon(x):
    for _ in range(7):
        tt.forward(x)
        tt.right(360/7)

draw_triangele(100)
draw_square(100)
draw_pentagon(100)
draw_hexagon(100)
draw_Heptagon(100)


screen = Screen()
screen.exitonclick()