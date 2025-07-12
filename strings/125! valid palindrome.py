import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

    def isPalindromeregex(self, s: str) -> bool:
        words = re.findall(r'[A-Za-z0-9]+', s)
        w = "".join(words).lower()
        print(w)
        l = 0
        r = len(w) -1
        while l <= r:
            if w[l] != w[r]:
                return False
            l+= 1
            r-=1
        return True

if __name__ == "__main__":
    sol = Solution()
    assert sol.isPalindrome("A man, a plan, a canal: Panama") == True, "Failed 1"
    assert sol.isPalindrome("race a car") == False, "Failed 1"
    assert sol.isPalindrome("0P") == False, "Failed 1"

    print("all tests passed")