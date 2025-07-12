class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        print(words)
        print(words[-1])
        return len(s.split()[-1])

if __name__ == "__main__":
    sol = Solution()
    assert sol.lengthOfLastWord("   fly me   to   the moon  ") == 4, "Failed 1"
    print("all tests passed")