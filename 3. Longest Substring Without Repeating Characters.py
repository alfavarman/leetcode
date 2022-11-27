"""Given a string s, find the length of the longest
substring
 without repeating characters.
 """


def lengthOfLongestSubstring(s: str) -> int:
    s_set = set()
    ss = ''
    results = []
    for i in s:
        if i in s_set:
            results.append(len(ss))

        ss += i
        s_set.add(i)
    return max(results)

s = "abcabcbb"

print(lengthOfLongestSubstring(s))
