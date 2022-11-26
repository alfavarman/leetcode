arr = [9, 2, 3, 4, 8, 3, 5, 7, 1, 0]
arr1 = ['d', 'r', 'w', 'a', 'u']


def get_bubblesort(arr: list, reverse: bool = False) -> list:
    indexes = len(arr)
    for i in range(indexes):
        for index in range(indexes - 1):
            if arr[index] > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]

    if reverse:
        arr = arr[::-1]
    return arr


def get_insertionsort(arr: list, reverse: bool = False) -> list:
    indexes = len(arr)

    for i in range(1, indexes):
        value = arr[i]
        previous = i - 1

        while previous >= 0 and arr[previous] > value:
            arr[previous + 1] = arr[previous]
            previous -= 1

        arr[previous + 1] = value

    if reverse:
        arr = arr[::-1]
    return arr


print(get_insertionsort(arr))
