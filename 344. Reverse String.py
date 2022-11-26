"""Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory."""

s = ["h","e","l","l","o"]

def reverseString(s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    for i in range(len(s)-2, -1, -1):
        s.append(s.pop(i))


reverseString(s)
print(s)





fastes:
class Solution:
    def reverseString(self, s: List[str]) -> None:
        self.reverse_lst(s, 0, len(s) - 1)

    def reverse_lst(self, lst, start, end):
        while start < end:
            lst[start], lst[end] = lst[end], lst[start]
            start += 1
            end -= 1




memory:


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        lo = 0
        hi = len(s) - 1

        while lo < hi:
            s[lo], s[hi] = s[hi], s[lo]
            lo += 1
            hi -= 1