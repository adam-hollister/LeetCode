"""
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.
"""
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in range(0,len(s)):
            item = s[i]
            if stack and stack[-1].lower() == item.lower() and stack[-1] != item:
                stack.pop()
            else:
                stack.append(item)
        ans = "".join(stack)
        return ans

if __name__ == "__main__":
    sol = Solution()
    assert sol.makeGood("leEeetcode") == "leetcode", "Test Case 1 Failed"
    assert sol.makeGood("abBAcC") == "", "Test Case 2 Failed"
    assert sol.makeGood("s") == "s", "Test Case 3 Failed"

    print("All test cases passed!")