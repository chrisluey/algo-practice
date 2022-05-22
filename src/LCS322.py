class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        acc, stuff, visited = 0, set(), [False] * (amount + 1)
        stuff.add(amount)
        while len(stuff) > 0:
            temp = set()
            acc += 1
            for j in stuff:
                for i in coins:
                    curr = j - i
                    if curr == 0:
                        return acc
                    elif curr > 0:
                        if visited[curr] == False:
                            temp.add(curr)
                            visited[curr] = True
            stuff = temp
        return -1 