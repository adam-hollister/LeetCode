class Solution:
    def numplusminus1(self, nums:list) -> list:
        answer = []
        my_hashset = set(nums)
        for x in my_hashset:
            if not(x+1 in my_hashset or x-1 in my_hashset):
                print("pass %s" % x)
                answer.append(x)
        return answer

if __name__ == "__main__":
    sol = Solution()

    assert sol.numplusminus1([1,7,2,3,5,7]) == [5,7], "Test Case 1 Failed"

    print("All test cases passed!")