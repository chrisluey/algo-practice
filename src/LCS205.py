class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for index in range(len(s)):
            if s_dict.get(s[index]) == None and t_dict.get(t[index]) == None:
                s_dict[s[index]] = t[index]
                t_dict[t[index]] = s[index]
            elif s_dict.get(s[index]) != t[index] or t_dict.get(t[index]) != s[index]:
                return False
        return True