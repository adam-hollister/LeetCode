class Solution:
    def countingelements(self, arr:list) -> int:
        total = 0
        my_hashset = set(arr)
        for i in range(len(arr)):
            if arr[i]+1 in my_hashset:
                total += 1
        return total

    def veryCoolSolution(self, arr: list) -> int:
        my_hashset = set(arr)
        return sum(1 for x in arr if x + 1 in my_hashset)

    def experimental(self, arr:list) -> int:
        total = 0
        my_hashmap = {}
        right = len(arr)-1
        while right >= 0:
            x = arr[right]
            if x in my_hashmap:
                my_hashmap[x] += 1
            else:
                my_hashmap[x] = 1
            if x+1 in my_hashmap:
                total += my_hashmap[x+1]
            right -= 1
        return total

if __name__ == "__main__":
    sol = Solution()

    assert sol.countingelements([1,2,3,0]) == 3, "Test Case 1 Failed"
    assert sol.countingelements([1,1,3,3,5,5,7,7]) == 0, "Test Case 2 Failed"

    print("all tests passed")