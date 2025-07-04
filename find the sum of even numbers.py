
class Solution:
    def rotate(self) -> int:
        k = 50/2
        print(k * (k+1))
        return sum(x for x in range(1,51) if x%2 == 0)

if __name__ == "__main__":
    sol = Solution()
    print(sol.rotate())
