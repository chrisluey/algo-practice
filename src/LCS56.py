class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        result = []
        intervals.sort()
        last = 0
        curr = intervals[0]
        max_num = curr[1]
        for i in range(1,len(intervals)):
            if max_num >= intervals[i][0]:
                max_num = max(max_num,intervals[i][1])
                last = 1
                continue
            else:
                result.append([curr[0], max_num])
                last = 0
                if i < len(intervals):
                    last = 1
                    curr = intervals[i]
                    max_num = curr[1]
        if last == 1:
            result.append([curr[0], max_num])
        return result