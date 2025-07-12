from functools import lru_cache

class Solution:
    def canJump(self, nums: list[int]) -> bool:#greedy
        farthest = 0
        for i in range(len(nums)):
            if i > farthest: #you dont have enough to make it to i so your done
                return False
            farthest = max(farthest, i + nums[i])
        return True

    def canJumpSlow(self, nums: list[int]) -> bool: #runs linear
        @lru_cache(None)
        def dfs(i:int) -> bool:
            if i >= len(nums) -1:
                return True
            for step in range(1, nums[i] + 1):
                if dfs(i + step):
                    return True
            return False
        return dfs(0)

    def canJumpOld(self, nums: list[int]) -> bool:#runs exponentially because of the splicing of the list
        if not nums or len(nums) == 1:
            return True
        for step in range(1, nums[0] + 1):
            if self.canJump(nums[step:]):
                return True
        return False

if __name__ == "__main__":
    sol = Solution()
    assert sol.canJump([0]) == True, "test 0 failed"
    assert sol.canJump([2,3,1,1,4]) == True, "test 1 failed"
    assert sol.canJump([3,2,1,0,4]) == False, "test 2 failed"
    assert sol.canJump([3,2,2,0,4]) == True, "test 3 failed"
    print("all success")