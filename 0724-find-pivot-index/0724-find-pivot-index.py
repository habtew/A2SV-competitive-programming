class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pref_arr = []
        pre = 0

        for i in range(len(nums)):
            pre += nums[i]
            pref_arr.append(pre)
        suf_arr = []
        suf = 0
        for i in range(len(nums) - 1, -1, -1):
            suf += nums[i]
            suf_arr.append(suf)
        for i in range(len(nums)):
            if pref_arr[i] == suf_arr[len(nums) - i - 1]:
                return i
        return -1