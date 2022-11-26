weights = "100 180 90 56 65 74 68 86 99"
arr1 = ["d", "r", "w", "a", "u"]


def insertion_sort(arr: list, dsc: bool = False) -> list:
    indicies = len(arr)

    for i in range(1, indicies):
        value = arr[i]
        previous = i - 1
        while previous >= 0 and arr[previous] > value:
            arr[previous + 1] = arr[previous]
            previous -= 1

        arr[previous + 1] = value

    if dsc:
        arr = arr[::-1]

    return arr


print(insertion_sort(arr1))
