class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        capped_count = [0] * (n + 1)  # count[i] = number of papers with i citations (capped at n)

        for c in citations:
            if c >= n:
                capped_count[n] += 1  # count papers with citations >= n this is the cap
            else:
                capped_count[c] += 1

        total = 0
        for h_index in range(n, -1, -1): # start at the best case and work down
            total += capped_count[h_index]
            if total >= h_index: # find the largest h_index that has a greater than or equal amount of other h_index's combined
                return h_index

        return 0

if __name__ == "__main__":
    sol = Solution()
    assert sol.hIndex([1,1,2,3,4]) == 2, "test 0 failed"
    assert sol.hIndex([3,0,6,1,5]) == 3, "test 1 failed"
    assert sol.hIndex([1,3,1]) == 1, "test 2 failed"
    assert sol.hIndex([2]) == 1, "test 3 failed"
    assert sol.hIndex([2,2]) == 2, "test 4 failed"
    assert sol.hIndex([3,5,3]) == 3, "test 5 failed"
    assert sol.hIndex([2,5,2]) == 2, "test 6 failed"
    assert sol.hIndex([2,5,2,4,4,4,4]) == 4, "test 7 failed"
    print("all success")