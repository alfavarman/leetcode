"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.



Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.


Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""
import timeit
import time


# class Solution:
#     def sortedSquares(self, nums: list[int]) -> list[int]:
#         result = []
#         for n in nums:
#             result.append(n*n)
#         result.sort()
#         return result

# class Solution:
#     def sortedSquares(self, nums: list[int]) -> list[int]:
#         return sorted(([x * x for x in nums]))


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        l, r = 0, len(nums) - 1
        result = []

        while l < r:
            if nums[l]**2 > nums[r]**2:
                result.insert(0, (nums[l]**2))
                l += 1
            elif nums[l]**2 < nums[r]**2:
                result.insert(0, (nums[r]**2))
                r -= 1
            else:
                result.insert(0, (nums[r]**2))
                result.insert(0, (nums[l]**2))
                r -= 1
                l += 1
        result.insert(0, (nums[r] ** 2))

        return result

class Solution1:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        l, r = 0, len(nums) - 1
        result = []

        while l < r:
            if abs(nums[l]) > abs(nums[r]):
                result.insert(0, (nums[l]**2))
                l += 1
            elif abs(nums[l]) < abs(nums[r]):
                result.insert(0, (nums[r]**2))
                r -= 1
            else:
                result.insert(0, (nums[r]**2))
                result.insert(0, (nums[l]**2))
                r -= 1
                l += 1
        result.insert(0, (nums[r] ** 2))

        return result

class Solution2:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        l, r = 0, len(nums) - 1
        result = []

        while l <= r:
            if abs(nums[l]) >= abs(nums[r]):
                result.insert(0, (nums[l] ** 2))
                l += 1
            else:
                result.insert(0, (nums[r] ** 2))
                r -= 1

        return result


class Solution3:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        l, r = 0, len(nums) - 1
        result = []

        while l <= r:
            if abs(nums[l]) >= abs(nums[r]):
                result.append(nums[l] ** 2)
                l += 1
            else:
                result.append(nums[r] ** 2)
                r -= 1

        return result[::-1]


nums = [-4, -1, 0, 3, 10]


start_time = time.time()
result = Solution()
result.sortedSquares(nums)
end_time = time.time()
time_solution = end_time - start_time

start_time = time.time()
result1 = Solution1()
end_time = time.time()
result1.sortedSquares(nums)
time_solution_1 = end_time - start_time

start_time = time.time()
result2 = Solution2()
result2.sortedSquares(nums)
end_time = time.time()
time_solution_2 = end_time - start_time

start_time = time.time()
result3 = Solution3()
end_time = time.time()
print(result3.sortedSquares(nums))
time_solution_3 = end_time - start_time

print(f"runtime of solution was: {time_solution}")
print(f"runtime of solution_1 was: {time_solution_1}")
print(f"runtime of solution_2 was: {time_solution_2}")
print(f"runtime of solution_3 was: {time_solution_3}")


time_solution = timeit.timeit(lambda: result.sortedSquares(nums), number=10000)
time_solution_1 = timeit.timeit(lambda: result1.sortedSquares(nums), number=100000)
time_solution_2 = timeit.timeit(lambda: result2.sortedSquares(nums), number=100000)
time_solution_3 = timeit.timeit(lambda: result3.sortedSquares(nums), number=100000)

print(f"runtime of solution   10000 was: {time_solution:.8f}")
print(f"runtime of solution_1 10000 was: {time_solution_3:.8f}")
print(f"runtime of solution_2 10000 was: {time_solution_3:.8f}")
print(f"runtime of solution_3 10000 was: {time_solution_3:.8f}")