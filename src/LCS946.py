class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i, j = 0, 0
        while 0 <= i < len(pushed) and j < len(popped):
            if pushed[i] != popped[j]:
                i += 1
            else:
                j += 1
                pushed.pop(i)
                if i > 0:
                    i -= 1
        return j >= len(popped)