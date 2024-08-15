import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
#tim.speed("fastest")
# extract the colors from image
# import colorgram

# colors = colorgram.extract('Day_18_Turtle_&_the_Graphical_User_Interface(GUI)/image.jpg', 30)

# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
    
# print(rgb_colors)


color_list = [(253, 251, 249), (253, 250, 253), (249, 250, 252), (236, 248, 243), (36, 95, 183), (236, 165, 79), (244, 223, 87), (215, 69, 105), (98, 197, 234), (250, 51, 22), (203, 70, 21), (240, 106, 143), (185, 47, 90), (143, 233, 216), (252, 136, 166), (165, 175, 233), (66, 45, 13), (72, 205, 170), (83, 187, 100), (20, 156, 51), (24, 36, 86), (252, 220, 0), (164, 28, 8), (105, 39, 44), (250, 152, 2), (22, 151, 229), (108, 213, 249), (254, 12, 3), (38, 48, 98), (98, 96, 186)]

class turtle_draw_dot:
    
    def __init__(self) -> None:
        self.yaxis = 0
    
    def choice_color(self):
        return random.choice(color_list)
        
    def draw_dot(self):
        for _ in range(10):
            tim.penup()
            tim.forward(50)
            tim.pendown()
            tim.dot(20, self.choice_color())
            tim.penup()
        self.yaxis += 50
        print(self.yaxis)

    def new_line(self):
        tim.setpos(0, self.yaxis)
    
draw = turtle_draw_dot()
for _ in range(10):
    draw.draw_dot()
    draw.new_line()
