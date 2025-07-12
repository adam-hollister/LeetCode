class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        idx1 = 0
        idx2 = len(numbers) -1
        while idx1 < idx2:
            num1 = numbers[idx1]
            num2 = numbers[idx2]
            total = num1 + num2
            if total == target:
                return [idx1 + 1, idx2 + 1]
            elif total > target:
                idx2 -= 1
            elif total < target:
                idx1 += 1
        return []

if __name__ == "__main__":
    sol = Solution()
    assert sol.twoSum([2,7,11,15], 9) == [1,2], "Failed 1"
    assert sol.twoSum([2,3,4], 6) == [1,3], "Failed 2"
    assert sol.twoSum([-1,0], -1) == [1,2], "Failed 2"
    assert sol.twoSum([0,0,3,4], 0) == [1,2], "Failed 2"
    print("all tests passed")