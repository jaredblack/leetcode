def evalRPN(tokens: list[str]) -> int:
    operand_stack = []
    for token in tokens:
        if token[-1].isdigit():
            operand_stack.append(int(token))
        else:
            operator = token
            op1 = operand_stack.pop()
            op2 = operand_stack.pop()
            if operator == "+":
                res = op1 + op2
            elif operator == "*":
                res = op1 * op2
            elif operator == "/":
                res = int(op2 / op1)
            elif operator == "-":
                res = op2 - op1
            operand_stack.append(res)
    return operand_stack[-1]
        
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))