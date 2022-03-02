class Solution:
    def simplifyPath(self, path: str) -> str:
         
        split = [p for p in path.split("/") if p != "." and p != ""]
        stack = []
        print(split)
        for ele in split:
            if ele == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(ele)
        return "/" + "/".join(stack)