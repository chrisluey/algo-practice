class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        first, second = False, False
        if len(flowerbed) == 1:
            return flowerbed[0] == 0 or n <= 0
        for i in range(len(flowerbed)):
            if first:
                if (i == 1 or i == len(flowerbed) - 1) and flowerbed[i] == 0:
                    n -= 1
                    first = True
                    continue
                if second:
                    if flowerbed[i] == 0:
                        n -= 1
                        first = True
                    else:
                        first = False
                    second = False
                else:
                    if flowerbed[i] == 0:
                        second = True
                    else:
                        first = False
            else:
                if flowerbed[i] == 0:
                    first = True
        return n <= 0