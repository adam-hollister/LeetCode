
class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = current_end = farthest = 0
        for i in range(len(nums) - 1): #don't jump from the last index
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps

if __name__ == "__main__":
    sol = Solution()
    assert sol.jump([0]) == 0, "test 1 failed"
    assert sol.jump([1,2]) == 1, "test 2 failed"
    assert sol.jump([2,3,1,1,4]) == 2, "test 3 failed"
    assert sol.jump([2,3,0,1,4]) == 2, "test 4 failed"
    assert sol.jump([2,1,1,1,4]) == 3, "test 5 failed"
    assert sol.jump([2,3,1]) == 1, "test 6 failed"
    assert sol.jump([1]) == 0, "test 7 failed"
    assert sol.jump([1,1,1,1]) == 3, "test 8 failed"
    print("all success")