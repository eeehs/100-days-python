# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

Total_days = 32850
Total_Weeks = 4680
Total_months = 1080 

my_days = Total_days - int(age) * 365
my_Weeks = Total_Weeks - int(age) * 52
my_months = Total_months - int(age) * 12

print(f"you have {my_days} days, {my_Weeks} weeks, and {my_months} months left.")