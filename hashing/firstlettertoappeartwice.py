class Solution:
    def firstlettertoappeartwice(self, s:str) -> str:
        my_hashset = set()
        for c in s:
            if c in my_hashset:
                return c
            my_hashset.add(c)
        return " "

if __name__ == "__main__":
    sol = Solution()

    assert sol.firstlettertoappeartwice("hello") == "l", "Test Case 1 Failed"

    print("all tests passed")