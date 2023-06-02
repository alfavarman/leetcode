import pytest
from solution_file import ListNode, Solution

class SolutionTest:
    def test_removeNthFromEnd_case1(self):
        # Create a sample linked list [1, 2, 3, 4, 5]
        values = [1, 2, 3, 4, 5]
        nodes = [ListNode(val) for val in values]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        head = nodes[0]

        solution = Solution()
        result = solution.removeNthFromEnd(head, 2)

        # Check if the resulting linked list is [1, 2, 3, 5]
        expected_values = [1, 2, 3, 5]
        expected_nodes = [ListNode(val) for val in expected_values]
        for i in range(len(expected_nodes) - 1):
            expected_nodes[i].next = expected_nodes[i + 1]
        expected_result = expected_nodes[0]

        assert self.linked_list_to_list(result) == self.linked_list_to_list(expected_result)

    def test_removeNthFromEnd_case2(self):
        # Create a sample linked list [1, 2]
        values = [1, 2]
        nodes = [ListNode(val) for val in values]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        head = nodes[0]

        solution = Solution()
        result = solution.removeNthFromEnd(head, 1)

        # Check if the resulting linked list is [1]
        expected_values = [1]
        expected_nodes = [ListNode(val) for val in expected_values]
        for i in range(len(expected_nodes) - 1):
            expected_nodes[i].next = expected_nodes[i + 1]
        expected_result = expected_nodes[0]

        assert self.linked_list_to_list(result) == self.linked_list_to_list(expected_result)

    # Helper function to convert linked list to a list
    def linked_list_to_list(self, head):
        result = []
        curr = head
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result

# Run the tests
if __name__ == '__main__':
    pytest.main()
