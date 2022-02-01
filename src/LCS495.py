class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        result, poison = 0, -1
        
        for shot in timeSeries:
            if shot > poison:
                result += duration
            else:
                result += shot + duration - 1 - poison
            poison = shot + duration - 1
        return result