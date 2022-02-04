class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def tryCombo(candidates: List[int], target: int, curr: List[int]) -> None:
            if target < 0:
                return
            elif target == 0:
                result.append(curr)
                return
            else:
                for i in range(len(candidates)):
                    tryCombo(candidates[i:], target - candidates[i], curr +[candidates[i]])
        tryCombo(candidates, target, [])
        
        
        return result