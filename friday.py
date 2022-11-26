# weights - # "100 180 90 56 65 74 68 86 99"  sort by sum and if sum same alphabetically
weights = "100 180 90 56 65 74 68 86 99"


def sort_by_sum_digits(strn: str) -> str:
    tokens = strn.split()

    sorted_tokens = sorted(tokens, key=lambda x: sum(int(i) for i in x))

    return " ".join(sorted_tokens)

