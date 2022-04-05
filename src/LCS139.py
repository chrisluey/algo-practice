class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        result = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                if len(w) <= i + 1 and s[i + 1 - len(w):i + 1] == w:
                    if i - len(w) < 0 or result[i - len(w)] == True:
                        result[i] = True
        return result[-1]