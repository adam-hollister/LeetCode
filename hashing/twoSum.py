class Solution:

    def twoSum(self, lst, target):
        my_hashmap = {}
        for i in range(len(lst)):
            if target - lst[i] in my_hashmap:
                return [my_hashmap[target - lst[i]], i]
            my_hashmap[lst[i]] = i
        return None

    def twoSumSet(self, lst, target):
        my_hashset = set()
        for item in lst:
            if target - item in my_hashset:
                return [target - item, item]
            my_hashset.add(item)
        return None

    def twoSumBool(self, lst, target):
        my_hashset = set()
        for item in lst:
            if target - item in my_hashset:
                return True
            my_hashset.add(item)
        return False

if __name__ == "__main__":
    sol = Solution()

    assert sol.twoSum([2,7,11,15], 9) == [0,1], "Test Case 1 Failed"
    assert sol.twoSum([3,2,4], 6) == [1,2], "Test Case 2 Failed"
    assert sol.twoSum([3,3], 6) == [0,1], "Test Case 3 Failed"

    assert sol.twoSumSet([2,7,11,15], 9) == [2,7], "Test Case 1 Failed"
    assert sol.twoSumSet([3,2,4], 6) == [2,4], "Test Case 2 Failed"
    assert sol.twoSumSet([3,3], 6) == [3,3], "Test Case 3 Failed"

    assert sol.twoSumBool([2, 7, 11, 15], 16) == False, "Test Case 1 Failed"
    assert sol.twoSumBool([3, 2, 4], 6) == True, "Test Case 2 Failed"
    assert sol.twoSumBool([3, 3], 6) == True, "Test Case 3 Failed"

    print("All test cases passed!")
