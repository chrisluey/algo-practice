# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        
        firstBad = n
        if isBadVersion(1):
            return 1
        else:
            lastGood = 1
        while firstBad - lastGood > 1:
            mid = (firstBad + lastGood) / 2
            if isBadVersion(mid):
                firstBad = mid
            else:
                lastGood = mid
        
        return int(firstBad)
        
        