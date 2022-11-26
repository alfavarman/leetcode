class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        for n in range(len(nums)):
            result.append(sum(nums[: n + 1]))
        return result

    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
