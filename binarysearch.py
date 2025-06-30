"""
I have to prove I am not a loser by being able to implement binary search
I Did it I am not a loser
"""
from collections import defaultdict
class Solution:
    def binarySearch(self, nums: list[int], target:int, offset:int = 0) -> int:
        #find the midpoint
        idx = len(nums) //2
        midpoint = nums[idx]
        if target == midpoint:
            return idx + offset
        elif target > midpoint: #remove left
            return self.binarySearch(nums[idx +1:], target, idx+1)
        else: #remove right
            return self.binarySearch(nums[:idx], target, offset)

# if __name__ == "__main__":
#     sol = Solution()
#     #assert sol.binarySearch([1,2,4,5,7,8,9,10], 7) == 4, "Test Case 1 Failed"
#     assert sol.binarySearch([1,2,4,5,7,8,9,10], 8) == 5, "Test Case 1 Failed"
#     print("All test cases passed!")

print("hello")