import pytest
from m_189_rotate_array import Solution, Solution1, Solution2


test_data = [
    ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
    ([0, 1, 2, 3, 4], 2, [3, 4, 0, 1, 2]),
    ([10, 20, 30, 40, 50], 1, [50, 10, 20, 30, 40]),
    ([], 0, []),
    ([1, 2, 3, 4, 5], 0, [1, 2, 3, 4, 5]),
    ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
    ([-1, -2, -3, -4, -5], 2, [-4, -5, -1, -2, -3]),
    ([10, -20, 30, -40, 50], 3, [-20, 30, -40, 50, 10])
]

class TestSolution:
    @pytest.mark.parametrize("nums, k, expected", test_data)
    def test_rotate(self, nums, k, expected):
        solution = Solution()
        solution.rotate(nums, k)
        assert nums == expected

class TestSolution1:
    @pytest.mark.parametrize("nums, k, expected", test_data)
    def test_rotate(self, nums, k, expected):
        solution1 = Solution1()
        solution1.rotate(nums, k)
        assert nums == expected

class TestSolution2:
    @pytest.mark.parametrize("nums, k, expected", test_data)
    def test_rotate(self, nums, k, expected):
        solution2 = Solution2()
        solution2.rotate(nums, k)
        assert nums == expected
