class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        n = len(num)
        def backtrack(i, curr_value, prev_value, expr):
            if i == n:
                if curr_value == target:
                    res.append(''.join(expr))
                return

            for j in range(i, n):
                cur_str = num[i:j+1]
                cur_num = int(cur_str)

                if len(cur_str) > 1 and cur_str[0] == '0':
                    break

                if i == 0:
                    backtrack(j+1, cur_num, cur_num, [cur_str])
                else:
                    backtrack(j+1, curr_value + cur_num, cur_num, expr + ['+', cur_str])
                    
                    backtrack(j+1, curr_value - cur_num, -cur_num, expr + ['-', cur_str])
                    
                    backtrack(j+1, curr_value - prev_value + prev_value * cur_num, prev_value * cur_num, expr + ['*', cur_str])

        backtrack(0, 0, 0, [])
        return res