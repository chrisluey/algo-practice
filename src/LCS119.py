class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        else:
            result = [1,1]
            while rowIndex > 1:
                curr = []
                for i in range(len(result) - 1):
                    curr.append(result[i] + result[i+1])
                curr.insert(0,1)
                curr.append(1)
                result = list(curr)
                rowIndex -= 1
            return result