class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        balance = 0

        for num in nums:
            print("candidate :", candidate," balance :",balance)
            if balance == 0:
                candidate = num
            balance +=1 if num == candidate else -1
        print("Winner:",candidate)
        return candidate

if __name__ == "__main__":
    sol = Solution()
    assert sol.majorityElement([2,2,2,4,4,2,2,4,4,2,1,1,2,1,2,2,3,3,2]) == 2, "test 1 failed"
    print("all pass")