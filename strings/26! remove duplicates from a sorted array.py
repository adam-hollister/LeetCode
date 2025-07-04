class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        write_index = 1
        for read_index in range(1, len(nums)):
            if nums[read_index] != nums[write_index - 1]:
                nums[write_index] = nums[read_index]
                write_index += 1

        return write_index
if __name__ == "__main__":
    sol = Solution()

    nums1 = [0,0,1,1,1,2,2,3,3,4]
    assert sol.removeDuplicates(nums1) == 5, "Failed 1"

    print("all tests passed")
