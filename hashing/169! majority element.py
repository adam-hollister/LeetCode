class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counts = {}

        max_key = 0
        max_value = 0

        for key in nums:
            counts[key] = counts.get(key, 0) + 1
            if max_value < counts[key]:
                max_key = key
                max_value = counts[key]
        return max_key

if __name__ == "__main__":
    sol = Solution()
    assert sol.majorityElement([3,2,3]) == 3, "failed 1"
    assert sol.majorityElement([2,2,1,1,2,2]) == 2, "failed 2"
    print("all success")