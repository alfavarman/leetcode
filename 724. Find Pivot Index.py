def pivotIndex(nums: list[int]) -> int:
    # l = 0
    # r = len(nums) - 1
    # sl = nums[0]
    # sr = nums[r]
    # while r > l:
    #     if sl == sr and r - l == 2:
    #         return r - 1
    #     elif sl > sr:
    #         r -= 1
    #         sr += nums[r]
    #     elif sl < sr:
    #         l += 1
    #         sl += nums[l]
    # return -1

    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i + 1 :]):
            return i
    return -1

    left, right = 0, sum(nums)
    for i, n in enumerate(nums):
        left += n
        if left == right:
            return i
        right -= n
    return -1


nums = [1, 7, 3, 6, 5, 6]

print(pivotIndex(nums))
