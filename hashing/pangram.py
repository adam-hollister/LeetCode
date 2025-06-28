class Solution:
    def pangram(self, s:str) -> bool:
        return len(set(s)) == 26

if __name__ == "__main__":
    sol = Solution()

    assert sol.pangram("thequickbrownfoxjumpsoverthelazydog") == True, "Test Case 1 Failed"
    assert sol.pangram("thequickbrownfoxjumpsovertheazydog") == False, "Test Case 1 Failed"

    print("All test cases passed!")