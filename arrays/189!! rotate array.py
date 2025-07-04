from collections import deque

class Solution:
    def rotate(self, nums: list[int], k: int) -> list[int]:
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        return nums

    def rotate1(self, nums: list[int], k: int) -> list[int]:
        queue = deque(nums)
        for i in range(k):
            queue.appendleft(queue.pop())
        q=list(queue)
        return q

if __name__ == "__main__":
    sol = Solution()
    assert sol.rotate([1,2,3,4,5,6,7],3) == [5,6,7,1,2,3,4], "test 1 failed"
    assert sol.rotate([-1,-100,3,99],2) == [3,99,-1,-100], "test 2 failed"
    print("all success")