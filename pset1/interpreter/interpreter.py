def calculate(expression):
    x, y, z = expression.split(" ")

    x = int(x)
    z = int(z)

    match y:
        case "+":
            return float(x + z)
        case "-":
            return float(x - z)
        case "*":
            return float(x * z)
        case "/":
            if (z == 0):
                return "Can't divide by Zero :("
            return round(x / z, 1)
        case _:
            return "Invalid Operator :("


def main():
    expression = input("Expression: ")
    print(calculate(expression))


if __name__ == "__main__":
    main()
