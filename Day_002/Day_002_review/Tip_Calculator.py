print("""
###############################
  Welcometo the tip calculator
###############################
""")

Total_Bill = float(input("What was the total bill? $"))
Tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
Total_People = int(input("How many people to split the bill? "))


### (Total_Bill + Total_bill에 대한 Tip) / Total_People

Total = (Total_Bill + Total_Bill * (Tip/100)) / Total_People

Should_pay = round(Total,2)

print(f"Each person should pay: ${Should_pay}")


