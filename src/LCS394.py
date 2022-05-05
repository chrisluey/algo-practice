class Solution:
    def decodeString(self, s: str) -> str:
        result, stack, numStack, currStr, c = [], [], [], [], 0
        while c < len(s):
            if s[c].isdigit():
                num = [s[c]]
                c += 1
                while s[c].isdigit() and c < len(s):
                    num.append(s[c])
                    c += 1
                numStack.append(int(''.join(num)))
            elif s[c] == "[":
                stack.append(currStr)
                currStr = []
                c += 1
            elif s[c] == "]":
                m = numStack.pop()
                if len(stack) > 0:
                    currStr = stack.pop() + (m * currStr)
                else:
                    result.extend(m * currStr)
                    currStr = []
                c += 1
            else:
                currStr.append(s[c])
                c += 1
        result.extend(currStr)
        return ''.join(result)