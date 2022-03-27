class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        first, second, third = True, True, True
        for i in range(len(word)):
            if i == 0:
                if word[i].isupper():
                    second = False
                else:
                    first, third = False, False
            else:
                if word[i].isupper():
                    second, third = False, False
                else:
                    first = False
            if  not first and not second and not third:
                break
        return first or second or third