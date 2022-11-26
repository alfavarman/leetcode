"""Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such
that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space."""



numbers = [0,0,3,4]
target = 0
numbers1 = [2,7,11,15]
target1 = 9

numbers2 = [2,3,4]
target2 = 6

numbers3 = [-1, 0]
target3 = -1


def twoSum(numbers: list[int], target: int) -> list[int]:
    # TIME COMPLEXITY 0(N^2)
    # for i in range(len(numbers)):
    #     for i2 in range(i+1, len(numbers)):
    #         if numbers[i2] + numbers[i] == target:
    #             return [i + 1, i2 + 1]

    # l = 0
    # r = len(numbers) -1
    # while l < r :
    #     if numbers[r] + numbers[l] == target:
    #         return [l + 1, r + 1]
    #     if numbers[r] + numbers[l] > target:
    #         r -= 1
    #     else:
    #         l += 1



    dic = {}
    for i in range(len(numbers)):
        if numbers[i] not in dic:
            dic[target - numbers[i]] = i
        else:
            return dic[numbers[i]] + 1, i + 1





print(twoSum(numbers, target))
