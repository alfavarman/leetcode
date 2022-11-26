def order_weight(strng):
    tokens = strng.split(" ")
    if len(tokens) == 0:
        return ""

    def sum_digits(strn: str) -> int:
        result = 0
        for i in strn:
            result += int(i)
        return result

    tokens.sort()
    sorted_tokens = sorted(tokens, key=sum_digits)
    result = " ".join(sorted_tokens)
    return result


def order_weight(_str):
    return " ".join(
        sorted(sorted(_str.split(" ")), key=lambda x: sum(int(c) for c in x))
    )


def sum_string(s):
    sum = 0
    for digit in s:
        sum += int(digit)
    return sum


def order_weight(strng):
    # your code
    initial_list = sorted(strng.split())
    result = " ".join(sorted(initial_list, key=sum_string))

    return result


def weight_key(s):
    return (sum(int(c) for c in s), s)


def order_weight(s):
    return " ".join(sorted(s.split(" "), key=weight_key))
