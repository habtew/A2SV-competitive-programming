class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        # find the peak of the mountain
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        
        peak = left
        # peak can not be the first and last index
        if peak == 0 or peak == len(arr) - 1:
            return False
        
        # search in first half
        for i in range(peak):
            print(arr[i], arr[i + 1], arr[i] <= arr[i + 1])
            if arr[i] >= arr[i + 1]:
                return False
        # search in second half
        for i in range(peak, len(arr) - 1):
            if arr[i] <= arr[i + 1]:
                return False

        return True