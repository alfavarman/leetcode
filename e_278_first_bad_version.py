# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# binary search
# left pointer -- latest isGood
# right pointer -- earliest isBad
# calculate mid -- if isGood, adjust left; otherwise, adjust right
# at end of loop, return either isLeft + 1 or isLeft


class Solution:
    def firstBadVersion(self, n: int) -> int:
        if isBadVersion(1):
            return 1

        latestGood = 1
        earliestBad = n

        while latestGood < earliestBad - 1:
            mid = math.floor((earliestBad - latestGood) / 2) + latestGood

            if isBadVersion(mid):
                earliestBad = mid
            else:
                latestGood = mid

        return earliestBad


class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        while low < high:
            mid = low + (high - low) // 2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return low
