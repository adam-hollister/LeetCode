"""
You have some number of sticks with positive integer lengths.
These lengths are given as an array sticks, where sticks[i] is the length of the ith stick.

You can connect any two sticks of lengths x and y into one stick by paying a cost of x + y.
You must connect all the sticks until there is only one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.
"""
import heapq
import math
class Solution:
    def connectSticks(self, sticks: list[int]) -> int:
        heapq.heapify(sticks)
        cost = 0
        while len(sticks) > 1:
            x = heapq.heappop(sticks)
            y = heapq.heappop(sticks)
            cost += x + y
            heapq.heappush(sticks, x+y)
        return cost

if __name__ == "__main__":
    sol = Solution()
    assert sol.connectSticks([2, 4, 3]) == 14, "Test Case 1 Failed"
    assert sol.connectSticks([1,8,3,5]) == 30, "Test Case 1 Failed"
    assert sol.connectSticks([5]) == 0, "Test Case 1 Failed"
    print("All test cases passed!")
