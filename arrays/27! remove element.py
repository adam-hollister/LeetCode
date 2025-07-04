class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        #filtered = [x for x in nums if x != val]
        #nums[:len(filtered)] = filtered
        #return len(filtered)
        k = 0
        while k < len(nums):
            if nums[k] == val:
                nums.remove(val)
            else:
                k+=1
        return k


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    nums = [3,2,2,3]
    val = 3
    expected = [2,2]
    k = sol.removeElement(nums, val)
    assert k == len(expected), "Test 1 failed: wrong length"
    assert sorted(nums[:k]) == sorted(expected), "Test 1 failed: wrong values"

    # Test Case 2
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    expected = [0,1,4,0,3]
    k = sol.removeElement(nums, val)
    assert k == len(expected), "Test 2 failed: wrong length"
    assert sorted(nums[:k]) == sorted(expected), "Test 2 failed: wrong values"

    print("All test cases passed!")