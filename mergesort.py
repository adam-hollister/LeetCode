class Solution:
    def merge(self, input_arr:list, left_half:list, right_half:list):
        i = j = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                input_arr[i+j] = left_half[i]
                i+=1
            else:
                input_arr[i+j] = right_half[j]
                j+=1
        while i < len(left_half):
            input_arr[i+j] = left_half[i]
            i+=1
        while j < len(right_half):
            input_arr[i+j] = right_half[j]
            j+=1

    def mergeSort(self, input_arr:list):
        if len(input_arr) < 2:
            return

        mid_index = len(input_arr) // 2
        left_arr = input_arr[0:mid_index]
        right_arr = input_arr[mid_index:len(input_arr)]
        print("left ", left_arr, " right ", right_arr)

        self.mergeSort(left_arr)
        self.mergeSort(right_arr)
        self.merge(input_arr, left_arr, right_arr)

if __name__ == "__main__":
    sol = Solution()
    arr1 = [4, 7, 2, 0, 1, 7]
    sol.mergeSort(arr1)
    assert arr1 == [0, 1, 2, 4, 7, 7], "test 1 failed"  # ✅ check in-place result
    print("all test pass")