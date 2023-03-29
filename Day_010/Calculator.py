
# Calculator 

# Add
def add(n1, n2):
    return n1 + n2

# Subtract 
def subtract(n1, n2):
    return n1 - n2

# Multply
def multply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

# Dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multply,
    "/": divide,
}
# 반복되는 함수
def cal():
    global num1
    global calculator
    while True:
        for i in operations:
            print(i)
        pick_operations = input("Pick an operation: ")
        num2 = int(input("What's the second number?: "))
        answer = operations[pick_operations](num1, num2)
        print(f"{num1} {pick_operations} {num2} = {answer}")

        continue_calculate = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if continue_calculate == "y":
            num1 = answer
            continue
        elif continue_calculate == "n":
            break
        else:
            print("종료합니다.")
            calculator = False
            break

from art import logo
calculator = True
print(logo)
while calculator:
    num1 = int(input("What's the first number?: "))
    cal()
    

