# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head


        end = head
        node_count = 1
        # aPointer to discover the end (or travers until next.next is None)
        while end.next:
            end = end.next
            node_count += 1

        node_to_del = node_count - n

        if not head.next or node_to_del == 0:
            return head.next


        def removeNthNode(head: Optional[ListNode], node_to_del: int) -> None:
            node = head
            # get to node need to be overwrite
            for n in range(1, node_to_del):
                node = node.next

            #node_to_del = node.next
            node.next = node.next.next

            #del node_to_del

        removeNthNode(head=head, node_to_del=node_to_del)
        return head


class Solution1:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        end_p = modify_p = head

        for _ in range(n):
            end_p = end_p.next

        if not end_p:
            return head.next

        while end_p.next:
            modify_p = modify_p.next
            end_p = end_p.next

        # end_p = modify_p.next
        modify_p.next = modify_p.next.next
        # required in C not in Python due to GC
        # del end_p
        return head



head = ListNode
pointer = head

for n in range(1, 2):
    pointer.val = n
    pointer.next = ListNode(n+1)
    pointer = pointer.next

r = Solution()
r.removeNthFromEnd(head, 2)

pointer = head

while pointer is not None:
    print(f"{pointer.val} --> ", end="")
    pointer = pointer.next