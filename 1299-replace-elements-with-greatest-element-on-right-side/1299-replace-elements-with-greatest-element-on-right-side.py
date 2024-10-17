class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right = -1
        # loop from right
        for i in range(len(arr) - 1, -1, -1):
            current_value = arr[i]
            arr[i] = max_right
            max_right = max(max_right, current_value) 

        return arr