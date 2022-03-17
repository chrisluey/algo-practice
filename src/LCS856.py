class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        result = 0
        stack = []
        for i in s:
            if i == "(":
                stack.append(0)
            else:
                curr = stack.pop()
                if len(stack) > 0:
                    stack[-1] += max(1, 2 * curr)
                else:
                    result += max(1, 2 * curr)
        return result