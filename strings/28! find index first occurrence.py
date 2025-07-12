import re


class Solution:

    def strStr2(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1

    def strStrwithbuiltinfunction(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

    def strStrregx(self, haystack: str, needle: str) -> int:
        parts = re.split(f'({re.escape(needle)})', haystack)
        total = 0
        for part in parts:
            if part == needle:
                return total
            total += len(part)
        return -1

if __name__ == "__main__":
    sol = Solution()
    assert sol.strStr("sadbutsad", "sad") == 0, "Failed 1"
    assert sol.strStr("leetcode", "leeto") == -1, "Failed 1"
    print("all tests passed")