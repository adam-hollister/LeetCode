"""
You are given a 0-indexed integer array piles, where piles[i] represents the number of stones in the ith pile,
and an integer k.
You should apply the following operation exactly k times:
    Choose any piles[i] and remove ceil(piles[i] / 2) stones from it.
Notice that you can apply the operation on the same pile more than once.
Return the minimum possible total number of stones remaining after applying the k operations.
ceil(x) is the smallest integer that is greater than or equal to x (i.e., rounds x up).
hint #1 Choose the pile with the maximum number of stones each time.
"""
import heapq
import math
class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        heap = [-pile for pile in piles]
        heapq.heapify(heap)

        for i in range(k):
            largest = -heapq.heappop(heap)
            reduced = math.ceil(largest / 2)
            heapq.heappush(heap, -reduced)
        return -sum(heap)

if __name__ == "__main__":
    sol = Solution()
    assert sol.minStoneSum([5,4,9], 2) == 12, "Test Case 1 Failed"
    assert sol.minStoneSum([4,3,6,7], 3) == 12, "Test Case 1 Failed"
    print("All test cases passed!")
