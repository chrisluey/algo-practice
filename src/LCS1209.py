class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if len(stack) == 0:
                stack.append((c, 1))
            elif stack[-1][0] == c:
                stack[-1] = (c, stack[-1][1] + 1)
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append((c, 1))
        resultStr = ""
        for i in stack:
            resultStr += i[0] * i[1]
        return resultStr