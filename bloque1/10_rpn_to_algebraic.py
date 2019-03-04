# encoding: utf-8

OPERATORS = set(['+', '-', '*', '/', '(', ')'])
PRIORITY = {'+':1, '-':1, '*':2, '/':2}


def postfix_to_infix(formula):
    formula = formula.split(' ')
    stack = []
    prev_op = None
    for ch in formula:
        if not ch in OPERATORS:
            stack.append(ch)
        else:
            b = stack.pop()
            a = stack.pop()
            expr = '('+a + ' ' + ch + ' ' + b+')'
            stack.append(expr)
            prev_op = ch
    return stack[-1]


# if __name__ == '__main__':
#     postfix_to_infix('1')
