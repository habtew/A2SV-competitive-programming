class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []

        n = len(nums)
        def backtrack(i, curr_sum):
            if curr_sum == target:
                res.append(sol[:])
                return
            if i == n or curr_sum > target:
                return
            # do not pick
            backtrack(i + 1, curr_sum)

            # pick
            sol.append(nums[i])
            backtrack(i, curr_sum + nums[i])
            sol.pop()
        backtrack(0, 0)
        return res