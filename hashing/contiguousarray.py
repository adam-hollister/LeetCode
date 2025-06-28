"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
"""
from collections import defaultdict
from difflib import diff_bytes


class Solution:
    def contiguousarray(self, nums: list[int]) -> int:
        zero = one = res = 0
        dif_index = {} # count[1] - count[0] -> index
        for i, n in enumerate(nums):
            if n == 0:
                zero += 1
            else:
                one += 1

            if one - zero not in dif_index:
                dif_index[one - zero] = i

            if one == zero:
                res = one + zero
            else:
                idx = dif_index[one - zero]
                res = max(res, i - idx)
        return res

    def findMaxLength(self, nums: list[int]) -> int:
        nums = [-1 if num == 0 else 1 for num in nums]
        running_sum = 0
        index_hashmap = {0: -1}  # running_sum -> earliest index
        max_length = 0

        for i, num in enumerate(nums):
            running_sum += num

            if running_sum in index_hashmap:
                # Calculate the length of the subarray from first occurrence to current index
                length = i - index_hashmap[running_sum]
                if length > max_length:
                    max_length = length
            else:
                # First time seeing this running sum, store the index
                index_hashmap[running_sum] = i

        return max_length


if __name__ == "__main__":
    sol = Solution()
    #assert sol.contiguousarray([0, 1]) == 2, "Test Case 1 Failed"
    assert sol.contiguousarray([0,1,0]) == 2, "Test Case 2 Failed"
    #assert sol.contiguousarray([0,1,1,1,1,1,0,0,0]) == 6, "Test Case 3 Failed"
    print("All test cases passed!")
