class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(index: int, path: List[str], string: str, res: List[str]):
            if len(path) > 4:
                return
            elif index >= len(string) and len(path) == 4:
                res.append(".".join(path))
                return
            else:
                for i in range(1, 4):
                    if index + i > len(string):
                        return
                    curr = string[index:index + i]
                    if i > 1 and curr[0:1] == "0":
                        continue
                    ip = int(curr)
                    if 255 >= ip >= 0:
                        backtrack(index + i, path + [curr], string, res)
        result = []
        backtrack(0, [], s, result)
        return result