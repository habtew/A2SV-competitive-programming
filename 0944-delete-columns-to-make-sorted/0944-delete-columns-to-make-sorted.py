class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for c in range(len(strs[0])):
            for i in range(1, len(strs)):
                if strs[i][c] < strs[i - 1][c]:
                    count += 1
                    break
                
        return count