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