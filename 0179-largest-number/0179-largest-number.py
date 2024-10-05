class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def sorting(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        # convert to list
        s = list(map(str, nums))
        s.sort(key=cmp_to_key(sorting))
        ans = ''.join(s)
        
        return '0' if ans[0] == '0' else ans