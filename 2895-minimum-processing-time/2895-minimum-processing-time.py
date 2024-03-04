class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        n = len(processorTime)
        larg = 0

        for i in range(n):
            larg = max(larg, processorTime[i] + max(tasks[i * 4 : i * 4 + 4]))

        return larg