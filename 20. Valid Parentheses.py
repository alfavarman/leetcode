def isValid(s: str) -> bool:
    mapping = {")": "(", "]": "[", "}": "{"}
    stack = []
    for char in s:
        if mapping.get(char):
            if not stack:
                return False
            elif stack[-1] == mapping[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return not stack


s = "()"
print(isValid(s))
