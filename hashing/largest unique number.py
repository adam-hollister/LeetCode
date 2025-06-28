"""
Given an integer array nums,
return the largest integer that only occurs once.
If no integer occurs once, return -1.
"""
from collections import defaultdict
class Solution:
    def largestUniqueNumber(self, nums: list[int]) -> int:
        my_hashmap = defaultdict(int)
        for num in nums:
            my_hashmap[num] += 1
        largest = -1
        for num in my_hashmap:
            if my_hashmap[num] == 1 and num > largest:
                largest = num
        return largest

if __name__ == "__main__":
    sol = Solution()
    assert sol.largestUniqueNumber([5,7,3,9,4,9,8,3,1]) == 8, "Test Case 1 Failed"
    print("All test cases passed!")
