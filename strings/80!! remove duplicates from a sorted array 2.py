class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        write_index = 2
        for read_index in range(2, len(nums)):
            if nums[read_index] != nums[write_index -2]:
                nums[write_index] = nums[read_index]
                write_index += 1
        k = write_index
        return k
if __name__ == "__main__":
    sol = Solution()

    nums1 = [0,0,1,1,1,2,2,3,3,4]
    assert sol.removeDuplicates(nums1) == 9, "Failed 1"

    print("all tests passed")
