def rotate(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    nums_l = len(nums)
    k = k % nums_l
    nums.extend(nums[0:-k])
    for x in range(nums_l-k):
        nums.pop(0)
    #

    for x in range(k):
        nums.insert(0, nums.pop())

nums = [1,2,3,4,5,6,7,8,9,10]
print(nums)
rotate(nums, 3)
print(nums)