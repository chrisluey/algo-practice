class Solution:
    def isPalindrome(self, s: str) -> bool:
        this_list = []
        s = s.lower().replace(" ", "")
        s = ''.join(ch for ch in s if ch.isalnum())
        if len(s) <= 1:
            return True
        sw = len(s) // 2
        f = sw
        if len(s) % 2 != 0:
            f = sw + 1    
        for i in range(sw):
            this_list.append(s[i])
        for j in range(f, len(s)):
            check = this_list.pop()
            if check != s[j]:
                return False
            
        return len(this_list) == 0