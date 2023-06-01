"""
189. Rotate Array
Medium
14.3K
1.6K
Companies
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.



Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105


Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""
import time
import timeit
import random
import copy


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

class Solution1:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for _ in range(k):
            nums.insert(0, nums.pop())

class Solution2:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        def reverse(nums: list, start: int = 0, end: int = len(nums) - 1) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
                start += 1

        reverse(nums)
        reverse(nums, 0, (k - 1))
        reverse(nums, k)


def generate_random_asc_array(length, min_val, max_val):
    return sorted([random.randint(min_val, max_val) for _ in range(length)])


min_v = - (2 ** 31)
max_v = (2 ** 32) - 1
l = random.randint(1, 10**5)
arr_a = generate_random_asc_array(l, min_v, max_v)
arr_a_copy = copy.deepcopy(arr_a)
step_a = random.randint(0, 10**5)

# Create a list of solution instances
solutions = [Solution(), Solution1(), Solution2()]

# Perform timing measurements for each solution
timing_results = []
for solution in solutions:
    start = time.time()
    solution.rotate(arr_a_copy, step_a)
    stop = time.time()
    result_time = stop - start
    timing_results.append(result_time)
    arr_a_copy = copy.deepcopy(arr_a)  # Reset the copied array

# Print the timing results
for i, result_time in enumerate(timing_results):
    print(f"Solution {i+1} took: {result_time}")