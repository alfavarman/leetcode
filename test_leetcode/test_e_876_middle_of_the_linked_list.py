import pytest
from solution_file import ListNode, Solution, Solution1, Solution3

class SolutionTest:
    def create_linked_list(self, values):
        nodes = [ListNode(val) for val in values]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        return nodes[0]

    def test_middleNode_case1(self):
        # Create a sample linked list [1, 2, 3, 4, 5]
        head = self.create_linked_list([1, 2, 3, 4, 5])

        solution = Solution()
        result = solution.middleNode(head)

        # Check if the middle node is 3
        assert result.val == 3

    def test_middleNode_case2(self):
        # Create a sample linked list [1, 2, 3, 4, 5, 6]
        head = self.create_linked_list([1, 2, 3, 4, 5, 6])

        solution = Solution1()
        result = solution.middleNode(head)

        # Check if the middle node is 4
        assert result.val == 4

    def test_middleNode_case3(self):
        # Create a sample linked list [1, 2, 3, 4]
        head = self.create_linked_list([1, 2, 3, 4])

        solution = Solution3()
        result = solution.middleNode(head)

        # Check if the middle node is 3
        assert result.val == 3

# Run the tests
if __name__ == '__main__':
    pytest.main()
