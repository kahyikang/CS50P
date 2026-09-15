exp = input("Expression: ")

n1, op, n2 = exp.split()

n1 = float(n1)
n2 = float(n2)

match op:
    case "+":
        ans = n1 + n2
    case "-":
        ans = n1 - n2
    case "*":
        ans = n1 * n2
    case "/":
        ans = n1 / n2

print(format(ans, ".1f"))
