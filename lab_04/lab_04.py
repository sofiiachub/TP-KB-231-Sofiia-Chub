def precedence(op):
    match op:
        case '^': return 3
        case '*' | '/': return 2
        case '+' | '-': return 1
        case _: return 0

def selectedOperator(op, b, a):
    match op:
        case '+': return a + b
        case '-': return a - b
        case '*': return a * b
        case '/': return a / b
        case '^': return a ** b

def infixToPostfix(expression):
    stack = []
    output = []
    for char in expression:
        match char:
            case digit if digit.isdigit():
                output.append(digit)
            case '(':
                stack.append(char)
            case ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
            case operator:
                while stack and precedence(stack[-1]) >= precedence(operator):
                    output.append(stack.pop())
                stack.append(operator)

    while stack:
        output.append(stack.pop())

    return ''.join(output)

def evaluatePostfix(expression):
    stack = []
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            result = selectedOperator(char, b, a)
            stack.append(result)
    return stack[0]

def main():
    infixExpr = input("Enter a mathematical expression: ")
    postfixExpr = infixToPostfix(infixExpr)
    print("Reverse Polish Entry:", postfixExpr)
    result = evaluatePostfix(postfixExpr)
    print("Result:", result)

if __name__ == "__main__":
    main()
