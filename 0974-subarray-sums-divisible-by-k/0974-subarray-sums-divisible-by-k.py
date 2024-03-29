class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mod_dict = {0: 1}
        pre = 0
        count = 0
        for i in range(len(nums)):
            pre += nums[i]
            mod = pre % k
            if mod in mod_dict:
                count += mod_dict[mod]
                mod_dict[mod] += 1
            else:
                mod_dict[mod] = 1
        print(mod_dict, count)
        return count