import unittest

from search_insert_position__35__easy import Solution


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
    def test_element_found(self):
        nums = [1, 3, 5, 7, 9]
        target = 5
        expected_index = 2
        result = self.solution.searchInsert(nums, target)
        assert result == expected_index

    def test_element_not_found(self):
        nums = [1, 3, 5, 7, 9]
        target = 4
        expected_index = 2
        result = self.solution.searchInsert(nums, target)
        assert result == expected_index

    def test_element_append(self):
        nums = [1,3,5,6]
        target = 7
        expected_index = 4
        result = self.solution.searchInsert(nums, target)
        assert result == expected_index

if __name__ == '__main__':
    unittest.main()