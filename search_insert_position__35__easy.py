"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = r + (l - r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return l

#
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         low = 0
#         high = len(nums) - 1
#         while low <= high:
#             mid = low + (high - low) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] > target:
#                 high = mid - 1
#             else:
#                 low = mid + 1
#
#         return low
#
#
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#
#         left = 0
#         right = len(nums) - 1
#
#         while left <= right:
#             mid = (left + right) // 2
#
#             if nums == target:
#                 return nums
#
#             elif target > nums[mid]:
#                 left = mid + 1
#
#             else:
#                 right = mid - 1
#
#         return left
