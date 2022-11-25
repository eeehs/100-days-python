#Write your code below this line 👇
import math

coverage = 5
def number_of_cans(height, width):
    print(f"You'll need {math.ceil((height * width) / coverage)} cans of paint")


number_of_cans(3, 9) 







#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)