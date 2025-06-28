"""
Given a string text, you want to use the characters of text to form as many
instances of the word "balloon" as possible.

You can use each character in text at most once.
Return the maximum number of instances that can be formed.
"""
from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = defaultdict(int)
        for char in text:
            if char in {'b','a','l','o','n'}:
                counts[char] += 1
        balloon = 0
        while counts['b'] >= 1 and counts['a'] >= 1 and counts['l'] >= 2 and counts['o'] >= 2 and counts['n'] >= 1:
            counts['b'] -= 1
            counts['a'] -= 1
            counts['l'] -= 2
            counts['o'] -= 2
            counts['n'] -= 1
            balloon += 1
        return balloon


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxNumberOfBalloons("nlaebolko") == 1, "Test Case 1 Failed"
    assert sol.maxNumberOfBalloons("loonbalxballpoon") == 2, "Test Case 2 Failed"
    assert sol.maxNumberOfBalloons("leetcode") == 0, "Test Case 3 Failed"
    print("All test cases passed!")
