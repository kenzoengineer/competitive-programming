# Stack
def evalRPN(tokens):
    stack = []
    ops = set(["+","-","/","*"])
    for token in tokens:
        #print(token,stack)
        if token not in ops:
            stack.append(int(token))
            continue
        res = 0
        o2 = stack.pop(-1)
        o1 = stack.pop(-1)
        match token:
            case "+":
                res = o1 + o2
            case "-":
                res = o1 - o2
            case "*":
                res = o1 * o2
            case "/":
                res = int(o1 / o2)
        stack.append(res)
    return stack[0]