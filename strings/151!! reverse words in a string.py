class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        l.reverse()
        k =  " ".join(l)
        return k

if __name__ == "__main__":
    sol = Solution()
    assert sol.reverseWords("the sky is blue") == "blue is sky the", "Failed 1"
    print("all tests passed")