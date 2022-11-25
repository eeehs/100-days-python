# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI_weight = int(weight)
BMI_height = float(height)

BMI = int(BMI_weight // (BMI_height*BMI_height))

print(BMI)