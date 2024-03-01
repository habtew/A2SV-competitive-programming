class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []

        for i in range(len(arr), 1, -1):
            max_index = arr.index(max(arr[:i]))
            arr[:max_index + 1] = reversed(arr[:max_index + 1])
            result.append(max_index + 1)
            arr[:i] = reversed(arr[:i])
            result.append(i)

        return result