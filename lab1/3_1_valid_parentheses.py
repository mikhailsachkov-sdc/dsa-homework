class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        PARENTHESES_INDEX = {')': '(', ']': '[', '}': '{'} # close -> open
        for char in s:
            if char in PARENTHESES_INDEX.values():
                stack.append(char)
            else:
                if not stack or stack[-1] != PARENTHESES_INDEX[char]:
                    return False
                stack.pop()

        return not stack

