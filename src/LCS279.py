class Solution:
    def numSquares(self, n: int) -> int:        
        if int(math.sqrt(n) + 0.5) ** 2 == n:
            return 1
        i, ps = 1, []
        while i * i < n:
            ps.append(i * i)
            i += 1
        check, acc = {n}, 0
        while check:
            acc += 1
            temp = set()
            for start in check:
                for s in ps:
                    if start - s == 0:
                        return acc
                    if start - s > 0:
                        temp.add(start - s)
            check = temp
        return acc