class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        this_list = []
        j = 0
        list_s = list(s)
        for i in range(len(list_s)):
            if list_s[i] == ")":
                if len(this_list) > 0 and j < len(this_list) and this_list[j] < i:
                    j += 1
                else:
                    list_s[i] = ""
            elif list_s[i] == "(":
                this_list.append(i)
        for k in range(j,len(this_list)):
            list_s[this_list[k]] = ""
        
        return "".join(list_s)