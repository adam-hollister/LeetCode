class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest_seen = float("inf")
        max_profit = 0
        for price in prices:
            if price < lowest_seen:
                lowest_seen = price
            else:
                max_profit = max(max_profit, price - lowest_seen)
        return max_profit

if __name__ == "__main__":
    sol = Solution()
    assert sol.maxProfit([7,1,5,3,6,4]) == 5, "wrong 1"
    assert sol.maxProfit([7,6,4,3,1]) == 0, "wrong 2"
    assert sol.maxProfit([1,4,2]) == 3, "wrong 3"
    assert sol.maxProfit([3,2,6,5,0,3]) == 4, "wrong 4"

    print("all pass")
