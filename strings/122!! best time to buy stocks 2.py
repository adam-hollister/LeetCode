class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest_seen = float("inf")
        max_profit = total_profit = 0
        for price in prices:
            if price < lowest_seen or max_profit > price - lowest_seen:
                total_profit += max_profit
                max_profit = 0
                lowest_seen = price
            else:
                max_profit = max(max_profit, price - lowest_seen)
        return total_profit + max_profit

if __name__ == "__main__":
    sol = Solution()
    assert sol.maxProfit([2,1,2,0,1]) == 2, "wrong 0"
    assert sol.maxProfit([7,1,5,3,6,4]) == 7, "wrong 1"
    assert sol.maxProfit([1,2,3,4,5]) == 4, "wrong 2"
    assert sol.maxProfit([7,6,4,3,1]) == 0, "wrong 3"

    print("all pass")
