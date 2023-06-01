import unittest

from e_997_squares_of_sorted_array import Solution, Solution1, Solution2, Solution3


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
    def test_element_found(self):
        nums = [-4, -1, 0, 3, 10]
        expected_arr = [0, 1, 9, 16, 100]
        result = self.solution.sortedSquares(nums)
        assert result == expected_arr


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution1()
    def test_element_found(self):
        nums = [-4, -1, 0, 3, 10]
        expected_arr = [0, 1, 9, 16, 100]
        result = self.solution.sortedSquares(nums)
        assert result == expected_arr


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution2()
    def test_element_found(self):
        nums = [-4, -1, 0, 3, 10]
        expected_arr = [0, 1, 9, 16, 100]
        result = self.solution.sortedSquares(nums)
        assert result == expected_arr


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution3()
    def test_element_found(self):
        nums = [-4, -1, 0, 3, 10]
        expected_arr = [0, 1, 9, 16, 100]
        result = self.solution.sortedSquares(nums)
        assert result == expected_arr



if __name__ == '__main__':
    unittest.main()