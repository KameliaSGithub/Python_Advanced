import math
def evaluate_expression(expression):
    tokens = expression.split()
    numbers = []
    result = None
    for token in tokens:
        if token in "+-*/":
            if result is None:
                result = numbers.pop(0)
            operator = token
            while numbers:
                number = numbers.pop(0)
                if operator == "+":
                    result += number
                elif operator == "-":
                    result -= number
                elif operator == "*":
                    result *= number
                elif operator == "/":
                    result = math.floor(result / number)
        else:
            numbers.append(int(token))
    return result
expression = input().strip()
print(evaluate_expression(expression))