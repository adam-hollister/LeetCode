from typing import Any


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1         # Last element in nums1's valid section
        j = n - 1         # Last element in nums2
        k = m + n - 1     # Last index of nums1 (including 0s at the end)

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


if __name__ == "__main__":
    sol = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    sol.merge(nums1, 3, [2, 5, 6], 3)
    assert nums1 == [1, 2, 2, 3, 5, 6], "Failed 1"

    nums1 = [0]
    sol.merge(nums1, 0, [1], 1)
    assert nums1 == [1], "Failed 2"

    print("all tests passed")
