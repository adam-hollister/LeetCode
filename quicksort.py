class Solution:
    def quicksort(self, arr:list, low:int, high:int) -> list:
        if low >= high:
            return arr

        pivot = arr[high]

        leftPointer = low
        rightPointer = high

        while leftPointer < rightPointer:
            while arr[leftPointer]<=pivot and leftPointer < rightPointer:
                leftPointer+=1
            while arr[rightPointer]>=pivot and leftPointer<rightPointer:
                rightPointer-=1
            arr[leftPointer], arr[rightPointer] = arr[rightPointer], arr[leftPointer]

        arr[leftPointer], arr[high] = arr[high], arr[leftPointer]

        self.quicksort(arr, low, leftPointer-1)
        self.quicksort(arr, leftPointer+1, high)
        return arr

if __name__ == "__main__":
    sol = Solution()
    arr1 = [4,7,2,0,1,7]
    assert sol.quicksort(arr1,0,len(arr1)-1) == [0,1,2,4,7,7], "test 1 failed"
    print("all test pass")