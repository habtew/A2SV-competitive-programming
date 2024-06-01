class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        arr = []
        for time in timePoints:
            hour, minute = time.split(":")
            total_minute = int(hour) * 60 + int(minute)
            arr.append(total_minute)
        arr.sort()

        min_diff = min(arr[i + 1] - arr[i] for i in range(len(arr) - 1))
        min_diff = min(min_diff, arr[0] + 24 * 60 - arr[-1])

        return min_diff