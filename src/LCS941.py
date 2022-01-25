class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        curr, dec = arr[0], 0
        for i in range(1, len(arr)):
            if dec == 0:
                if arr[i] > curr:
                    curr = arr[i]
                elif arr[i] < curr:
                    if i > 1:
                        curr = arr[i]
                        dec = 1
                    else:
                        return False
                else:
                    return False
            else:
                if arr[i] < curr:
                    curr = arr[i]
                else:
                    return False
        return dec == 1