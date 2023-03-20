# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

position_row = position[1]
position_column = int(position[0])

 
if position_row == "1":
    row1[position_column-1] = "X"
elif position_row == "2":
    row2[position_column-1] = "X"
elif position_row == "3":
    row3[position_column-1] = "X"



print(f"{row1}\n{row2}\n{row3}")