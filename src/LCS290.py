class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        this_s_dict = {}
        this_p_dict = {}
        s_list = s.split()
        if len(s_list) != len(pattern):
            return False
        for i in range(len(s_list)):
            s_curr = this_s_dict.get(pattern[i])
            p_curr = this_p_dict.get(s_list[i])
            if s_curr == None and p_curr == None:
                this_s_dict[pattern[i]] = s_list[i]
                this_p_dict[s_list[i]] = pattern[i]
            elif s_curr != s_list[i] or p_curr != pattern[i]:
                return False
        return True