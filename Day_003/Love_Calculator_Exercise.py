# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()

# TRUE Count
T = name1.count("t") + name2.count("t")
R = name1.count("r") + name2.count("r")
U = name1.count("u") + name2.count("u")
E = name1.count("e") + name2.count("e")

true_count = str(T + R + U + E)

# LOVE Count 
L = name1.count("l") + name2.count("l")
O = name1.count("o") + name2.count("o")
V = name1.count("v") + name2.count("v")
E = name1.count("e") + name2.count("e")

love_count = str(L + O + V + E)

Love_point = int(true_count + love_count)

if Love_point < 10 or Love_point > 90:
    print(f"Your score is {Love_point}, you go together live coke and mentos.")
elif  40 < Love_point < 50:
    print(f"Your score is {Love_point}, you are alright together")
else:
    print(f"Your score is {Love_point}.")