def sortedSquares(nums: list[int]) -> list[int]:
    i = 4
    a = i^2
    a = [x*x for x in nums]
    i = sorted(a)

    return i


nums = [-4,-1,0,3,10]
print(sortedSquares(nums))