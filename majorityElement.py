from collections import defaultdict


def majorityElement(nums: list[int]) -> int:
    majority = len(nums) // 2

    frequency = defaultdict(int)

    for num in nums:
        frequency[num] += 1
        if frequency[num] > majority:
            return num







nums = [2,2,1,1,1,2,2]

nums1 = [3,2,3]

