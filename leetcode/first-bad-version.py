# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        first_bad_version = r
        while l <= r:
            m = (l + r) // 2

            if not isBadVersion(m):
                l = m + 1
            else:
                first_bad_version = min(first_bad_version, m)
                r = m - 1
        
        return first_bad_version