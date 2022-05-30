class Solution:
    def maxProduct(self, words: List[str]) -> int:
        result = 0
        wordSet = [None] * len(words)
        for i in range(len(words) - 1):
            if wordSet[i] == None:
                wordSet[i] = set(words[i])
            currI = wordSet[i]
            for j in range(i + 1, len(words)):
                if wordSet[j] == None:
                    wordSet[j] = set(words[j])
                currJ = wordSet[j]
                if len(currI.intersection(currJ)) == 0:
                    result = max(result, len(words[i]) * len(words[j]))
        return result