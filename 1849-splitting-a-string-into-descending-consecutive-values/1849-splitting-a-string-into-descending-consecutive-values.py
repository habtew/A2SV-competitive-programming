class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(index, prev_num, count):
            if index == len(s):
                return count > 1
            
            curr_num = 0
            for j in range(index, len(s)):
                curr_num = curr_num * 10 + int(s[j])
                
                if prev_num == -1 or prev_num - curr_num == 1:
                    if dfs(j + 1, curr_num, count + 1):
                        return True
                
            return False
        
        return dfs(0, -1, 0)