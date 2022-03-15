class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        this_list = []
        list_s = list(s)
        for i in range(len(list_s)):
            if list_s[i] == ")":
                if len(this_list) > 0:
                    this_list.pop(0)
                else:
                    list_s[i] = ""
            elif list_s[i] == "(":
                this_list.append(i)
        for j in this_list:
            list_s[j] = ""
        return "".join(list_s)