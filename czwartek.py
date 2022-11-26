from math import sqrt

# rpn - + - / * sqrt
# sorting - dont use libs
# weights - # "100 180 90 56 65 74 68 86 99"  sort by sum and if sum same alphabetically

# TASK 1
input1 = "3 4 2 + *"
input2 = "5 4 2 * 3 + + sqrt"
input3 = "3.12 4 + 2 *"


def calculate_rpn(strn: str) -> float:
    operators = ["+", "-", "*", "/"]

    stack = []
    for token in strn.split():
        if token in operators:
            b = stack.pop()
            stack.append(eval(f"{stack.pop()}{token}{b}"))
        elif token == "sqrt":
            stack.append(sqrt(stack.pop()))
        else:
            stack.append(token)

    return float(stack[0])


print(calculate_rpn(input1))
print(calculate_rpn(input2))
print(calculate_rpn(input3))


# Task 2
# sorting - dont use libs # bubble & insertion
arr1 = ["d", "r", "w", "a", "u"]


def get_bubble_sort(arr: list, desc: bool = False) -> list:
    indices = len(arr)
    for a in range(indices):
        for b in range(a, indices):
            if arr[a] < arr[b]:
                a, b = b, a

    if desc:
        arr = arr[::-1]

    return arr


def get_insertion_sort(arr: list, desc: bool = False) -> list:
    indices = len(arr)

    for i in range(1, indices):
        value = arr[i]
        previous = i - 1
        while previous >= 0 and arr[previous] > value:
            arr[previous + 1] = arr[previous]
            previous -= 1

        arr[previous + 1] = value

    if desc:
        arr = arr[::-1]

    return arr


print(get_insertion_sort(arr1))
print(get_bubble_sort(arr1))


# weights - # "100 180 90 56 65 74 68 86 99"  sort by sum and if sum same alphabetically
weights = "100 180 90 56 65 74 68 86 99"


def weights_sort(arr: str) -> str:
    # tokenise
    tokens = arr.split()

    # sort tokens
    tokens.sort()

    # sort by sum
    sorted_arr = sorted(tokens, key=lambda x: sum(int(i) for i in x))

    return " ".join(sorted_arr)


print(weights_sort(weights))
