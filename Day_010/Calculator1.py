
# Calculator

def add(n1, n2):
    return n1 + n2

#subtract

def subtract(n1, n2):
    return n1 - n2

# Multiply

def Multiply(n1, n2):
    return n1 * n2

# Divide

def Divide(n1, n2):
    return n1 / n2

operations = {
"+": add,
"-": subtract,
"*": Multiply,
"/": Divide
}

first_number = int(input("What's the first number?: "))
for oper in operations:
    print(oper)
operation_symbol = input("Pick an operation: ")
while operation_symbol not in operations:
    print("잘못 입력하셨습니다 다시 입력해주세요")
    operation_symbol = input("Pick an operation: ")
    if operation_symbol in operations:
        break
next_number = int(input("What's next number?: "))

Calculator = operations[operation_symbol]
answer = Calculator(first_number, next_number)
print(f"{first_number} {operation_symbol} {next_number} = {answer}")

continue_answer = True
while continue_answer:
    a = input(f"Type 'y' to contunue calculating with {answer}, or type 'n' to exit.: ")
    if a == "n":
        print("Calculator 종료")
        break
    operation_symbol = input("Pick another operation: ")
    while operation_symbol not in operations:
        print("잘못 입력하셨습니다 다시 입력해주세요")
        operation_symbol = input("Pick an operation: ")
        if operation_symbol in operations:
            break
    next_number = int(input("What's next number?: "))
    Calculator = operations[operation_symbol]
    next_answer = Calculator(answer, next_number)

    print(f"{answer} {operation_symbol} {next_number} = {next_answer}")
    answer = next_answer