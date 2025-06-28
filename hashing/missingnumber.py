class Solution:
    def missingnumber(self, nums:list) -> int:
        my_hashset = set(nums)
        for i in range(len(my_hashset)):
            if i not in my_hashset:
                return i
        return len(my_hashset)

    def missingnumberusingmath(self, nums: list) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        return expected_sum - sum(nums)


if __name__ == "__main__":
    sol = Solution()

    assert sol.missingnumber([3,0,1]) == 2, "Test Case 1 Failed"
    assert sol.missingnumber([0,1]) == 2, "Test Case 2 Failed"
    assert sol.missingnumber([9,6,4,2,3,5,7,0,1]) == 8, "Test Case 3 Failed"

    print("all tests passed")