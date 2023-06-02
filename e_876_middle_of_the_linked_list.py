"""
876. Middle of the Linked List
Easy
9.6K
283
Companies
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.



Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.


Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head

        counter = 1
        while pointer.next:
            pointer = pointer.next
            counter += 1

        pointer = head

        for _ in range(1, (counter // 2) + 1):
            pointer = pointer.next

        return pointer



class Solution1:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
        return(slow)



class Solution3:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        length = 0
        while current:
            length += 1
            current = current.next

        current = head

        for i in range(length // 2):
            current = current.next

        return current