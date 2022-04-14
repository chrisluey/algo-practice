class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        result = 0
        for i in ops:
            if i == "+":
                curr = stack[-2] + stack[-1]
                result += curr
                stack.append(curr)
            elif i == "D":
                curr = stack[-1] * 2
                result += curr
                stack.append(curr)
            elif i == "C":
                curr = stack.pop()
                result -= curr
            else:
                curr = int(i)
                result += curr
                stack.append(curr)
        return result