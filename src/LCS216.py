class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        def tryCombo(k: int, n: int, path: List[int], numbers: List[int], res: List[List[int]]):
            if len(path) > k or 0 > n:
                return
            if len(path) == k and 0 == n:
                res.append(path)
                return
            for i in range(len(numbers)):
                tryCombo(k, n - numbers[i], path + [numbers[i]], numbers[i + 1:], res)
        result = []
        tryCombo(k, n, [], options, result)
        return result