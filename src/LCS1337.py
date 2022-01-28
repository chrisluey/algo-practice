class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        this_dict = {}
        for i in range(len(mat)):
            this_dict[i] = sum(mat[i])
        result = sorted(this_dict, key=this_dict.get)
        return result[0:k]