from art import logo

print(logo)

first_number = float(input("What's the first number?: "))

print("""
+
-
*
/
""")

while True:
    operation = input("Pick an operation: ")
    if operation not in ["+","-","*","/"]:
        print("다시 입력하세요")
        continue
    next_number = float(input("What's the next number?: "))
    if operation == "+":
        result = first_number + next_number
        print(f"{first_number} + {next_number} = {result}")
    elif operation == "-":
        result = first_number - next_number
        print(f"{first_number} - {next_number} = {result}")
    elif operation == "*":
        result = first_number * next_number
        print(f"{first_number} * {next_number} = {result}")       
    else:
        result = first_number / next_number
        print(f"{first_number} / {next_number} = {result}")
    
    new_calculation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if new_calculation == "y":
        first_number = result
        continue
    elif new_calculation == "n":
        first_number = float(input("What's the first number?: "))
        continue
    else:
        print("게임을 종료하겠습니다.")
        break