from math import sqrt

input1 = '3 4 2 + *'            #4
input2 = '5 4 2 * 3 + + sqrt'   #18
input3 = '3.12 4 + 2 *'         #14.24


def get_tokens(maths: str) -> list:
    tokens = maths.split(sep=' ')
    return tokens


def get_rpn_result(tokens: list) -> float:
    operators = {'+': '+', '-': '-', '*': '*', '/': '/', 'sqrt': 'sqrt()'}
    while len(tokens) > 1:

        for index, token in enumerate(tokens):
            if token in operators:
                op = tokens.pop(index)
                if op == 'sqrt':
                    # b = tokens[index - 1]
                    tokens[index-1] = sqrt(tokens[index - 1])
                else:
                    a = tokens[index-2]
                    b = tokens.pop(index-1)
                    tokens[index-2] = eval(f'{a}{op}{b}')
                break

    return tokens[0]


print(get_rpn_result(get_tokens(input2)))