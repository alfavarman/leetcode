class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        indecis = len(nums)
        low = 0
        high = indecis - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return low


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums == target:
                return nums

            elif target > nums[mid]:
                left = mid + 1

            else:
                right = mid - 1

        return left
