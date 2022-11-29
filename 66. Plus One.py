

def plusOne(digits: list[int]) -> list[int]:
    i = -1
    while i >= -len(digits):
        if digits[i] != 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
            i -=1
    digits.insert(0, 1)
    return digits


# Fastes
def plusOne1(digits: list[int]) -> list[int]:
    result = []
    holder = 1
    for i in range(len(digits) - 1, -1, -1):
        temp = digits[i]
        digits[i] = (digits[i] + holder) % 10
        holder = (temp + holder) // 10

    if holder == 0:
        return digits
    else:
        return [1] + digits



#memory efficient
def plusOne2(self, arr: list[int]) -> list[int]:
    from collections import deque
    ans = deque(arr)

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] < 9:
            ans[i] = ans[i] + 1
            break

        else:
            if i == 0:

                ans[i] = 0
                ans.appendleft(1)
            else:
                ans[i] = 0

    return ans


arr = [1,2,3,4,5]
arr1 = [9]
arr2 = [1,9,9,9,9]
arr3 = [9,9,9]


print(plusOne(arr))
print(plusOne(arr1))
print(plusOne(arr2))
print(plusOne(arr3))