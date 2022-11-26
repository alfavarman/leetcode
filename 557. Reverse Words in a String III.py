"""Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

"""
s = "Let's take LeetCode contest"


def reverseWords(s: str) -> str:
    return ' '.join(token[::-1] for token in s.split())
    #     fastes:
    # return " ".join(s.split()[::-1])[::-1]

print(reverseWords(s))


