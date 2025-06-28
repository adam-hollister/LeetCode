"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?
"""
import heapq
from collections import defaultdict
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)
        for i in range(k-1):
            heapq.heappop(heap)
        return -heapq.heappop(heap)

if __name__ == "__main__":
    sol = Solution()
    assert sol.findKthLargest([3,2,1,5,6,4], 2) == 5, "Test Case 1 Failed"
    assert sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4, "Test Case 2 Failed"
    print("All test cases passed!")
