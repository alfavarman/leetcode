from math import sqrt
input1 = "3 4 2 + *"
input2 = "5 4 2 * 3 + + sqrt"
input3 = "3.12 4 + 2 *"


# def calc_rpn(strn: str) -> float:
#     # list of operators
#     operators = ['+', '-', '*', '/', 'sqrt']
#     # tokenise
#     tokens = strn.split(" ")
#
#     # loop tokens
#     while len(tokens) > 1:
#         for index, token in enumerate(tokens):
#             if token in operators:
#                 op = tokens.pop(index)
#                 if op == 'sqrt':
#                     tokens[index - 1] = sqrt(float(tokens[index-1]))
#                 else:
#                     a = tokens[index-2]
#                     b = tokens.pop(index-1)
#                     tokens[index-2] = eval(f'{a}{op}{b}')
#                 break
#
#     result = float(tokens[0])
#     return result
#
#
# print(calc_rpn(input2))


# def calc_RPN(strn: str) -> int:
#     strn_tokens = strn.split()
#     stack = []
#     for item in strn_tokens:
#         if item == '+':
#             stack.append(stack.pop() + stack.pop())
#         elif item == '-':
#             stack.append(stack.pop() - stack.pop())
#         elif item == '*':
#             stack.append(stack.pop() * stack.pop())
#         elif item == '/':
#             stack.append(stack.pop() / stack.pop())
#         elif item == "sqrt":
#             stack.append(sqrt(stack.pop()))
#         else:
#             stack.append(float(item))
#
#     result = stack[0]
#     return result



def calc_RPN(strn: str) -> int:
    operators = ['+', '-', '*', '/']
    strn_tokens = strn.split()
    stack = []
    for item in strn_tokens:
        if item in operators:
            stack.append(eval(f'{stack.pop()}{item}{stack.pop()}'))
        elif item == "sqrt":
            stack.append(sqrt(stack.pop()))
        else:
            stack.append(float(item))

    result = stack[0]
    return result


print(calc_RPN(input2))
