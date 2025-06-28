
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for part in path.split("/"):
            if part == "..":
                if stack:
                    stack.pop()
            elif part != "." and part != "":
                stack.append(part)

        ans = "/" + "/".join(stack)
        return ans

if __name__ == "__main__":
    sol = Solution()
    assert sol.simplifyPath("/home/") == "/home", "Test Case 1 Failed"
    assert sol.simplifyPath("/home//foo/") == "/home/foo", "Test Case 2 Failed"
    assert sol.simplifyPath("/home/user/Documents/../Pictures") == "/home/user/Pictures", "Test Case 3 Failed"
    assert sol.simplifyPath("/../") == "/", "Test Case 4 Failed"
    assert sol.simplifyPath("/.../a/../b/c/../d/./") == "/.../b/d", "Test Case 5 Failed"

    print("All test cases passed!")