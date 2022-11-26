"""Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the '
                                       'non-zero elements.

Note that you must do this in-place without making a copy of the array."""


def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for a in range(len(nums) - 2, -1, -1):
        if nums[a] == 0:
            nums.append(nums.pop(a))


nums = [0, 0, 1, 3, 12]
moveZeroes(nums)
print(nums)
